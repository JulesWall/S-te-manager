import discord
from config import *
from db.Player.checkers import *

from Discord.MessageSender import * 

class Command:

    def __init__(self, message, bot):
        self.message = message
        self.bot = bot
        self.channel = message.channel
        self.has_permission = True
        self.args = None

    async def not_permission(self):
        return None 

class AdminCommand(Command):

    def __init__(self, message, bot):
        Command.__init__(self, message, bot)
        self.has_permission = CommandRequired(self.message.author.id, "OWNER").has_permission
        

class GameCommand(Command):

    def __init__(self, message, bot):
        Command.__init__(self, message, bot)
        self.has_permission = CommandRequired(self.message.author.id, "player").has_permission
    
    async def not_permission(self):
        await MessageSender(self.message, self.bot).not_player()
        
        
class CtaCommand(Command):

    def __init__(self, message, bot):
        Command.__init__(self, message, bot)
        self.has_permission = CommandRequired(self.message.author.id, "cta").has_permission

class CommandRequired():

    def __init__(self, user_id, required):
        condition = {
            "OP":user_id in OP,
            "OWNER":user_id in OWNER,
            "cta":Checkers(user_id).is_cta(),
            "player":Checkers(user_id).is_player(),
        }
        self.has_permission = condition[required]
