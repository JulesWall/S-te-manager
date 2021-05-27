import discord
import asyncio

from config import *
from Discord.data import *
from db.classes.MoveTracker import *
from db.function.House import *

class MessageManager():

    def __init__(self, message, bot):
        self.message = message
        self.bot = bot
        self.rp_categories = rp_categories
        self.category_logement = 836028397880606760
        self.is_command, self.is_hrp, self.is_move = self.is_command(), self.is_hrp(), self.is_move()

    async def manage(self):
        if self.is_command:
            await self.get_command()
        if self.is_hrp:
            await __import__('asyncio').sleep(DELETETIME);await self.message.delete()
        if self.is_move:
            try: move = MoveTracker(self.message, self.bot)
            except: return None
            if move.hasMove():
                await move.move()
        if self.message.channel.category.id == self.category_logement:
            try: 
              house = ExistHouse(self.message.author.id)
              if house.channel == self.message.channel.id: house.refresh()
            except: pass
            
    def is_command(self):
        check = [
            self.message.content.startswith(PREFIX),
            IS_MAINTENANCE and self.message.author.id in MAINTENANCE_AUTHORIZE or not IS_MAINTENANCE,
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
            not self.message.author.bot
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
