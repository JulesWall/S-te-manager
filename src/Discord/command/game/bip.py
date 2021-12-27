import discord
from config import *

from Discord.command.Command import *
from db.Player.checkers import *
from db.function.Bip import BipInit, ExistBip
from db.function.ExistProfil import *
from Game.image.create import Bipimage

class Bip(GameCommand):

    def __init__(self, message, bot):
        GameCommand.__init__(self, message, bot)
        self.pid = self.message.author.id

    async def run(self):
        if not self.has_permission : return await self.not_permission()

        profil = ExistProfil(self.pid)
        if not Checkers(self.pid).own_pager(): BipInit(self.pid, "OFF")

        bip = ExistBip(self.pid)
        if bip.statut == "OFF" : path = Bipimage("OFF", self.pid).save()
        else : path = Bipimage("ON", self.pid).on(profil.name, bip.statut).save()
        self.file = discord.File(str(path))
        await self.message.channel.send(file=self.file)



