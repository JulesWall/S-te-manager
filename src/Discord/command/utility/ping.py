import discord 
from Discord.command.Command import *

class Ping(Command):

    def __init__(self, message, bot):
        Command.__init__(self, message, bot)

    async def run(self):
        if not self.has_permission : return await self.not_permission()

        import time
        now = time.monotonic()
        msg = await self.channel.send(f'Latence du bot :')
        ping = int((time.monotonic() - now) * 1000)
        await msg.edit(content=f'Latence du bot : ``{ping} ms``')