import discord

from db.function.Vehicule import Vehicule

class Statut():

    def __init__(self, message, bot):
        self.bot = bot
        self.message = message
        self.channel = message.channel

    async def run(self):

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
            print(e)
            await self.message.delete()
            msg = await self.channel.send("commande invalide")
            __import__('time').sleep(2)
            await msg.delete()
        
        

