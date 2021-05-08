import discord
import asyncio

from config import *
from Discord.data import *

class MessageManager():

    def __init__(self, message, bot):
        self.message = message
        self.bot = bot
        self.is_command = self.is_command()
        self.is_hrp = self.is_hrp()
        self.is_move = self.is_move()
        self.rp_categories = rp_categories
    
    async def manage(self):
        if self.is_command: 
            await self.get_command()
        if self.is_hrp:
            await __import__('asyncio').sleep(DELETETIME);await self.message.delete()
    
    def is_command(self):
        check = [
            self.message.content.startswith(PREFIX), 
            is_maintenance and self.message.author.id not in MAINTENANCE_AUTHORIZE,
            self.message.guild.id in SERVER_WHITELISTED,
            not self.message.author.bot
        ]
        return not False in check
    
    def is_hrp(self):
        check = [
            self.message.content.startswith('('),
            self.message.channel.category.id in self.rp_categories
        ]
        return not False in check
    
    def is_move(self):
        check = [
            self.message.channel.category.id in self.rp_categories and not self.message.content.startswith('('),            
        ]
        return not False in check
    
    async def get_command(self, dict_args=commands, indice=0):
        strc = str(self.message.content.split(" ")[indice][1:]).lower()

        found = []
        for key in dict_args.keys():
            found.append(key)
        
        for i in range(len(strc)):
            for key in dict_args.keys():
                try: assert key[i] == strc[i]
                except: 
                    if key in found:
                        found.remove(key)
            if len(strc) <= 1: break
        
        if len(found)==1: 
            await dict_args[found[0]][0](self.message, self.bot).run()
            
            