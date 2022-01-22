import discord
import discord.ui as dui
from config import *

from Discord.command.Command import *
from db.Player.checkers import *
from db.function.Bip import BipInit, ExistBip
from db.function.ExistProfil import *
from Game.image.create import Bipimage
from db.function.ExistWh import ExistWh

class Bip(GameCommand):

    def __init__(self, message, bot):
        GameCommand.__init__(self, message, bot)
        self.pid = self.message.author.id
        self.args1 = {
            "on":self.on,
            "off":self.off
        }

    async def run(self):
        if not self.has_permission : return await self.not_permission()
        self.profil = ExistProfil(self.pid)
        if not Checkers(self.pid).own_pager(): BipInit(self.pid, "OFF")

        async with self.message.channel.typing():
            self.bip = ExistBip(self.pid)
            await self.message.delete()
            if len(self.message.content.split()) == 1:
                if self.bip.statut == "OFF" : await self.off(f"**Décroche le bip de sa ceinture et le regarde**")
                else : await self.on(f"**Décroche le bip de sa ceinture et appuis sur le bouton pour en allumer l'écran**")
            else :
                try:
                    arg = await self.get_args(self.args1, 1) 
                    assert arg != None
                except: 
                    await self.error()
                    return None        
                await arg()       
            print("here")

    async def on(self, msg=f"**Allume son bip**"):
        if self.bip.statut != "OFF" and len(self.message.content.split()) != 1: 
            return await MessageSender(self.message, self.bot).wh(
                name = self.message.author.display_name,
                avatar_url=self.message.author.display_avatar.url,
                msg = "**Essaye d'allumer son bip avant de se rendre compte qu'il est déjà allumé**"
            )
        if self.bip.update("Disponible") : #has change (dans le update)
            self.profil.start_service(0)
            wh = ExistWh("cta")
            await MessageSender(self.message, self.bot).wh(wh.name, wh.link, f"(Début de service enregistrée pour <@{self.message.author.id}>)", self.message.channel)
        await MessageSender(self.message, self.bot).wh(
                name = self.message.author.display_name,
                avatar_url=self.message.author.display_avatar.url,
                msg = msg
            )
        self.path = Bipimage("ON", self.pid).on(self.profil.name, self.bip.statut).save()
        self.file = discord.File(str(self.path))

        self.view = add_items([
            dui.Button(style=discord.ButtonStyle.red, label="Éteindre le bip", emoji="<:bip:924613243496960030>"),
            dui.Button(style=discord.ButtonStyle.grey, label="          "),
            dui.Button(style=discord.ButtonStyle.red, label="SOS")
        ], [
            self.roff,
            self.rnothing,
            self.rnothing,
        ], dui.View()
        )

        await self.message.channel.send(file=self.file, view=self.view)

    async def off(self, msg=f"**Eteins son bip**"):
        if self.bip.statut == "OFF" and len(self.message.content.split()) != 1: 
            return await MessageSender(self.message, self.bot).wh(
                name = self.message.author.display_name,
                avatar_url=self.message.author.display_avatar.url,
                msg = "**Essaye d'éteindre son bip avant de se rendre compte qu'il est déjà éteins**"
            )
        if self.bip.update("OFF") : #has_change (dans le update)
            time_service = ((__import__("time").time() - self.profil.end_service())/60)
            self.profil.add_service_time(time_service)
            wh = ExistWh("cta")
            await MessageSender(self.message, self.bot).wh(wh.name, wh.link, f"(Fin de service enregistrée pour <@{self.message.author.id}>)", self.message.channel)
        await MessageSender(self.message, self.bot).wh(
                name = self.message.author.display_name,
                avatar_url=self.message.author.display_avatar.url,
                msg = msg
            )
        self.path = Bipimage("OFF", self.pid).save()
        self.file = discord.File(str(self.path))
        self.view = add_items([
            dui.Button(style=discord.ButtonStyle.green, label="Allumer le bip", emoji="<:bip:924613243496960030>"),
            dui.Button(style=discord.ButtonStyle.grey, label="          "),
            dui.Button(style=discord.ButtonStyle.grey, label="          ")
        ], [
            self.ron,
            self.rnothing,
            self.rnothing,
        ], dui.View())

        await self.message.channel.send(file=self.file, view=self.view)

    async def rnothing(self, interaction):pass
    
    async def ron(self, interaction):
        async with self.message.channel.typing():
           await interaction.message.delete()
           await self.on()

    async def roff(self, interaction):
        async with self.message.channel.typing():
           await interaction.message.delete()
           await self.off()

def add_items(buttons, r, v):
    i = 0
    for b in buttons: 
        b.callback = r[i]
        v.add_item(b)
        i += 1
    return v