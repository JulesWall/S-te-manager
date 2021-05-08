import discord
from config import *
from db.Player.checkers import *

class Command:

    def __init__(self, message, bot):
        self.message = message
        self.bot = bot
        self.has_permission = True
        self.args = None

class AdminCommand(Command):

    def __init__(self, message, bot):
        Command.__init__(self, message, bot)
        self.has_permission = CommandRequired(self.message.author.id, "OWNER")

class GameCommand(Command):

    def __init__(self, message, bot):
        Command.__init__(self, message, bot)
        self.has_permission = CommandRequired(self.message.author.id, "player")
        
class CtaCommand(Command):

    def __init__(self, message, bot):
        Command.__init__(self, message, bot)
        self.has_permission = CommandRequired(self.message.author.id, "cta")

class CommandRequired():

    def __init__(self, user_id, required):
        condition = {
            "OP":user_id in OP,
            "OWNER":user_id in OWNER,
            "cta":Checkers(user_id).is_cta(),
            "player":Checkers(user_id).is_player(),
        }
        self.required = condition[required]
        return self.required
