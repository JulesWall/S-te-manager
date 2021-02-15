import discord
from config import *

class Eval:
    def __init__(self, message : discord.Message, bot : discord.Client()):
        self.bot = bot
        self.message = message
        
    async def run(self):
        import time
        if self.message.author.id in OWNER:
            import os
            command = str(' '.join(self.message.content.split()[1:]))
            
            try:
                output = eval(command)
                msg = await self.message.channel.send(output)
            except Exception as e:
                error = "```{0}```".format(e)
                await self.message.channel.send(error)
