import discord 
from db.function.top import get_top
from config import *

from classes.checkers import *
from db.function.ExistProfil import *

class Pds():

    def __init__(self, message:discord.Message, bot:discord.Client()):

        self.bot = bot
        self.message = message
        self.player = ExistProfil(self.message.author.id)

    async def run(self):
        profil = ExistProfil(self.message.author.id)
        if Checkers(self.message.author.id).astreinte(): 
            time_service = ((__import__("time").time() - self.player.end_service())/60)
            await self.message.channel.send(f"Fin de service pour <@{self.message.author.id}>")
            salaire = self.player.update_money((round(((1.5**1.1)*time_service-1.56), 2)))
            CP = (round((-0.5*salaire), 2))
            if CP > 0: CP *= -1
            self.player.update_cp(CP)
            await self.message.channel.send(f"<@{self.message.author.id}> - Pendant votre service, vous avez gagné {salaire} € et perdus {CP*-1} % de condition physique.")
        else:
            if len(self.message.content.split()) > 1: 
                if Checkers(self.message.author.id).cta() and self.message.content.split()[1]=="cta": cta=1
                else: cta=0
            else: cta=0
            self.player.start_service(cta)
            if cta: await self.message.channel.send(f"Début de service au cta pour <@{self.message.author.id}>")
            else: await self.message.channel.send(f"Début de service pour <@{self.message.author.id}>")