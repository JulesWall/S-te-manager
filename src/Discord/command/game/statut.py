import discord

from Discord.command.Command import *
from db.function.Vehicule import Vehicule

class Statut(GameCommand):

    def __init__(self, message, bot):
        GameCommand.__init__(self, message, bot)

    async def run(self):
        if not self.has_permission : return await self.not_permission()

        try:
            vhlname = self.message.content.split(' ')[1]
            statut = self.message.content.split(' ')[2]
            assert int(statut) >= 0 
            assert int(statut) <= 8
            vhl = Vehicule(vhlname)
            vhl.statut = statut
            vhl.save()
            await self.message.delete()
        except Exception as e:
            self.error()
        
        

