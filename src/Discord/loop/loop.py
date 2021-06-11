import discord
import asyncio
import os

from config import IS_MAINTENANCE
from db.function.Tph import *
from db.function.House import *
from db.function.ExistWh import delete_expired_wh

class RLoop():

    def __init__(self, bot):
        self.bot = bot

    async def loop(self):
        while 1:

            delete_expired_tph()
            delete_expired_wh()

            chan_to_delete = delete_expired_house()
            for c in chan_to_delete:
                await self.bot.get_guild(705059899750613013).get_channel(c).delete()
                
            if not IS_MAINTENANCE:
                game = discord.Game("📵 CTA indisponible !")
                status=discord.Status.idle
                service = Querry("SELECT * FROM service")     
                for data in service:
                   cta = data[4]
                   if cta: game = 
                        discord.Game("📱 CTA disponible !")
                        status=discord.Status.online
                await self.bot.change_presence(status=status, activity=game)
            
            await asyncio.sleep(200)
