import math

import discord

from Discord.command.Command import *
from Discord.MessageSender import *
from db.function.Querry import Querry
from db.function.ExistWh import *
from db.function.WhInit import *
from db.Player.checkers import *
from config import FOOTER

class wh(CtaCommand):

    def __init__(self, message, bot):
        CtaCommand.__init__(self, message, bot)
        self.args1 = {
            "send":self.send,
            "new":self.new,
            "list":self.listt
        }

    async def run(self):
        if not self.has_permission : return await self.not_permission()

        try:
            arg = await self.get_args(self.args1, 1)
            assert arg != None
        except:
            await self.error()
            return None
        await arg()

    async def send(self):
        try:
            alias = self.message.content.split(" ")[2]
            wh = ExistWh(alias)
        except : return await self.error()

        await MessageSender(self.message, self.bot).wh(
            wh.name,
            wh.link,
            " ".join(self.message.content.split()[3:])
        )
        await self.message.delete()
        wh.update_lastuse()

    async def new(self):
        try:
            alias, name, link = ' '.join(self.message.content.split(" ")[2:]).split("|")
            WhInit(alias, name, link)
            await self.message.channel.send(f"Le webhook `{name}` avec l'url `{link}` et l'alias {alias} a bien été ajouté à la base de donnée. Il sera automatiquement supprimé si il n'est pas utilisé pendant plus de 30 jours. Vous pouvez le supprimer en le remplacant avec un autre webhook avec le même alias.")
        except Exception as e:
            await self.message.channel.send(e)
            return await self.error()

    async def listt(self):

        datas = Querry("SELECT alias FROM wh ORDER BY lastuse DESC")
        content = ""
        maxpages = math.ceil(len(datas)/25)

        try:
            page = int(self.message.content.split(" ")[2])
            if page>maxpages:
                page = maxpages
        except:
            page = 1

        for i in range(25*(page-1), 25*(page)):
            try : idwh = datas[i][0]
            except : break
            wh = ExistWh(idwh)
            content += f"\n **-** {wh.alias} > {wh.name}"

        content += f"\n\n Page `{page}`/`{maxpages}` | Do !wh list <p>"
        embed=discord.Embed(title="Liste des alias de WebHook (alias > nom)", description=f"{content}", color=0x00ffe1)
        embed.set_footer(text=FOOTER)
        await self.message.channel.send(embed=embed)
