import discord
from config import OWNER
from db.function.Querry import *
from classes.checkers import *
from Syno.Syno import *

class Eval:
    def __init__(self, message : discord.Message, bot : discord.Client()):
        self.bot = bot
        self.message = message
        
    async def run(self):
        import time
        if self.message.author.id in OWNER:
            import os
            command = str(' '.join(self.message.content.split()[1:]))
            
            try:
                output = await eval(command)
                msg = await self.message.channel.send(output)
            except TypeError:
                try:
                    output = eval(command)
                    msg = await self.message.channel.send(output)
                except Exception as e:
                    await self.message.channel.send(f"`ERROR`\n```{e}```")
            except Exception as e:
               await self.message.channel.send(f"`ERROR`\n```{e}```")


    async def test(self):
        for chan in self.message.guild.channels:
            await chan.set_permissions(self.message.guild.get_role(781962819590553600), send_messages=False, reason="cat>all")