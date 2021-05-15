import discord
from db.function.top import get_top
from config import *

from Discord.command.Command import *
from db.Player.checkers import *
from db.function.ExistProfil import *

class Pds(GameCommand):

    def __init__(self, message, bot):
        GameCommand.__init__(self, message, bot)

    async def run(self):
        if not self.has_permission : return await self.not_permission()

        profil = ExistProfil(self.message.author.id)
        if Checkers(self.message.author.id).is_astreinte():
            time_service = ((__import__("time").time() - profil.end_service())/60)
            await self.message.channel.send(f"Fin de service pour <@{self.message.author.id}>")
            salaire = 0 # self.player.update_money((round(((1.5**1.1)*time_service-1.56), 2)))
            CP = 0 #(round((-0.5*salaire), 2))
            if CP > 0: CP *= -1
            profil.update_cp(CP)
            profil.add_service_time(time_service)
            await self.message.channel.send(f"<@{self.message.author.id}> - Pendant votre service, vous avez gagné {salaire} € et perdus {CP*-1} % de condition physique.")
        else:
            if len(self.message.content.split()) > 1:
                if Checkers(self.message.author.id).is_cta() and self.message.content.split()[1]=="cta": cta=1
                else: cta=0
            else: cta=0
            profil.start_service(cta)
            if cta: await self.message.channel.send(f"Début de service au cta pour <@{self.message.author.id}>")
            else: await self.message.channel.send(f"Début de service pour <@{self.message.author.id}>")
