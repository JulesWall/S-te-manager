import discord
import asyncio 
import os

from Syno.Syno import *
class LoopSyno():

    def __init__(self, bot):
        self.bot = bot
    
    async def loop(self):
        while 1:
            channel = self.bot.get_guild(705059899750613013).get_channel(833676923409268812)
            Syno().run()
            os.chdir("/Users/Juels/Desktop/Github/csp/image")
            await channel.purge(limit=100)
            await asyncio.sleep(1)
            await channel.send("**Synoptiques des moyens:**")
            await channel.send(file=discord.File("syno1.png"))
            await channel.send(file=discord.File("syno2.png"))
            await asyncio.sleep(29)

        

