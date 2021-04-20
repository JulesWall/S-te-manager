
import discord
import time

from db.function.Querry import Querry
from db.function.ExistWh import *
from db.function.WhInit import *
from classes.checkers import *
from config import FOOTER

class wh():

    def __init__(self, message:discord.Message, bot:discord.Client()):

        self.bot = bot
        self.message = message

    async def run(self):
        try : assert Checkers(self.message.author.id).cta()
        except : return await self.error()
        try: command = self.message.content.split(" ")[1]
        except: self.error()
        if command == "s":
            try: 
                alias = self.message.content.split(" ")[2]
                wh = ExistWh(alias)
            except : return await self.error()

            try: webhooks = await self.message.channel.webhooks();webhook = webhooks[0]
            except Exception as e: webhook = await self.message.channel.create_webhook(name="sètebot")
            await webhook.send(content=" ".join(self.message.content.split()[3:]), username=wh.name, avatar_url=wh.link)
            await self.message.delete()
            wh.update_lastuse()

        elif command == "new":
            try:
                alias, name, link = ' '.join(self.message.content.split(" ")[2:]).split("|")
                WhInit(alias, name, link)
                await self.message.channel.send(f"Le webhook `{name}` avec l'url `{link}` et l'alias {alias} a bien été ajouté à la base de donnée. Il sera automatiquement supprimé si il n'est pas utilisé pendant plus de 30 jours. Vous pouvez le supprimer en le remplacant avec un autre webhook avec le même alias.")
            except Exception as e: await self.message.channel.send(e);return await self.error()
        
        elif command == "list":
            datas = Querry("SELECT alias FROM wh")
            content = ""
            for data in datas:
                wh = ExistWh(data[0]) 
                content += f"\n **-** {wh.alias} > {wh.name}"
            embed=discord.Embed(title="Wh list", description=f"{content}", color=0xa600ff)
            embed.set_footer(text=FOOTER)
            await self.message.channel.send(embed=embed)


        else:
            return await self.error()

    async def error(self):
        msg = await self.message.channel.send("Une erreur est survenue")
        __import__("time").sleep(5)
        await self.message.delete()
        await msg.delete()
        return None