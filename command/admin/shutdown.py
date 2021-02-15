import discord
from config import *

class ShutDown:
    def __init__(self,message : discord.Message, bot : discord.Client()):
        self.bot = bot
        self.message = message
        
    async def run(self):    
        if self.message.author.id in OWNER:
            await self.message.channel.send('Shut down')
            await self.bot.close()