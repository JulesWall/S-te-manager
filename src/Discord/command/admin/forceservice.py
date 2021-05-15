import discord

from Discord.command.Command import *
from db.function.ExistProfil import *
from db.Player.checkers import *

class ForceService(CtaCommand):

    def __init__(self, message, bot):
        CtaCommand.__init__(self, message, bot)

    async def run(self):
        if not self.has_permission : return await self.not_permission()

        try:
            target = int(self.message.content.split()[1])
        except:
            return await self.error()

        target = ExistProfil(target)
        if Checkers(target.idd).is_astreinte():
            ExistProfil(target.idd).end_service()
            await self.message.channel.send(f"Fin de service de <@{target.idd}>")
        else:
            ExistProfil(target.idd).start_service(0)
            await self.message.channel.send(f"Début de service de <@{target.idd}>")
