import discord
import asyncio

from config import *
from commands import commands

class Engine():

    def __init__(self, message, bot):
        self.message = message
        self.bot = bot
    
    async def run(self):
        has_prefix = self.message.content.startswith(PREFIX)
        if has_prefix:
            if is_maintenance and self.message.author.id not in MAINTENANCE_AUTHORIZE: return "break"
            elif self.message.guild.id in SERVER_WHITELISTED:
                try:
                    command_info = commands.get(self.message.content[1:].split()[0])
                    command = command_info[0]
                except:
                    pass
                await command(self.message, self.bot).run()
            else: pass
