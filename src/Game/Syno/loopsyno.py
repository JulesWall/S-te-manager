import discord
import asyncio
import os
from Game.Syno.Syno import *
from config import FILE_PATH

class LoopSyno():

    def __init__(self, bot):
        self.bot = bot

    async def loop(self):
        while 1:            
            channel = self.bot.get_guild(705059899750613013).get_channel(779375346855575582)
            await channel.trigger_typing()
            Syno().run()
            os.chdir(FILE_PATH + "/Game/image/")
            #await channel.purge(limit=100)
            await channel.send("**Synoptiques des moyens:**")
            await channel.send(file=discord.File("syno1.png"))
            #await channel.send(file=discord.File("syno2.png"))
            await asyncio.sleep(45)
