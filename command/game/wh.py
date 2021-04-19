
import discord
import time

from db.function.Querry import Querry
from db.function.ExistWh import *
from db.function.WhInit import *
from classes.checkers import *

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
                name = self.message.content.split(" ")[2]
                wh = ExistWh(name)
            except : return await self.error()

            try: webhooks = await self.message.channel.webhooks();webhook = webhooks[0]
            except Exception as e: webhook = await self.message.channel.create_webhook(name="sètebot")
            await webhook.send(content=" ".join(self.message.content.split()[3:]), username=wh.name, avatar_url=wh.link)
            await self.message.delete()
            wh.update_lastuse()

        elif command == "new":
            try:
                name, link = ' '.join(self.message.content.split(" ")[2:]).split("|")
                WhInit(name, link)
                await self.message.channel.send(f"Le webhook `{name}` avec l'url `{link}` a bien été ajouté à la base de donnée. Il sera automatiquement supprimé si il n'est pas utilisé pendant plus de 30 jours. Vous pouvez le supprimer en le remplacant avec un autre webhook du même nom.")
            except Exception as e: await self.message.channel.send(e);return await self.error()
        else:
            return await self.error()

    async def error(self):
        msg = await self.message.channel.send("Une erreur est survenue")
        __import__("time").sleep(5)
        await self.message.delete()
        await msg.delete()
        return None