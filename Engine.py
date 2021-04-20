import discord
import asyncio

from config import *
from commands import *
from classes.checkers import *
from classes.MoveTracker import *

class Engine():

    def __init__(self, message, bot):
        self.message = message
        self.bot = bot
    
    async def run(self):
        has_prefix = self.message.content.startswith(PREFIX)

        if Checkers(self.message.author.id).player() and not has_prefix:
            move = MoveTracker(self.message, self.bot)
            if move.isRP() and move.hasMove(): await move.move()

        if self.message.content.startswith('('):
            await __import__('asyncio').sleep(DELETETIME);await self.message.delete()
        
        if has_prefix:
            if is_maintenance and self.message.author.id not in MAINTENANCE_AUTHORIZE:return "break"
            elif self.message.guild.id in SERVER_WHITELISTED:
                if not self.message.content.startswith('!pr') and not Checkers(self.message.author.id).player():
                    await self.message.channel.send('Fais !profil pour t\'enregistrer');return "break"
                try:
                    command_info = commands.get(self.message.content[1:].split()[0])
                    command = command_info[0]
                except:
                    pass
                await command(self.message, self.bot).run()
            else:
                pass
