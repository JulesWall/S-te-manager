import discord
from config import *
from Discord.command.Command import *
from Discord.MessageSender import *

class ShutDown(AdminCommand):
    def __init__(self,message : discord.Message, bot : discord.Client()):
        AdminCommand.__init__(self, message, bot)
        
    async def run(self):    
        if not self.has_permission: return await self.not_permission()
        await self.message.channel.send(MessageSender(self.message, self.bot).bot("BOT_IS_GOING_DOWN"))
        await self.bot.close()
