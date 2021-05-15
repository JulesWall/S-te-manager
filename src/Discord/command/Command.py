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

    async def get_args(self, dict_args, indice):
        strc = str(self.message.content.split(" ")[indice]).lower()

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
            return dict_args[found[0]]

    async def error(self, msg="Un erreur est survenue"):
        msg = await self.message.channel.send(msg)
        await __import__("asyncio").sleep(DELETETIME)
        try:
            await self.message.delete()
            await msg.delete()
        except:
            pass
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
