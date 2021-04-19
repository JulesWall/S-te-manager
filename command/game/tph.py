
import discord

from db.function.Tph import *
from db.function.WhInit import *
from db.function.ExistProfil import *
from db.files.data import galonDB
from db.function.ExistWh import *
from classes.checkers import *
class Tph():

    def __init__(self, message:discord.Message, bot:discord.Client()):

        self.bot = bot
        self.message = message

    async def run(self):
        try: command = self.message.content.split(" ")[1]
        except : return self.error()

        if command == "take":
            if self.message.channel.id == 779375346855575582 and not Checkers(self.message.author.id).tph():
                tph = TphInit(self.message.author.id, self.message.channel.id, int(__import__("time").time()+60*60), "off")
                WhInit(f"tph-{self.message.author.display_name}", str(galonDB[ExistProfil(tph.id_owner).grade]))
                wh = ExistWh(f"tph-{self.message.author.display_name}")
                try: webhooks = await self.message.channel.webhooks();webhook = webhooks[0]
                except Exception as e: webhook = await self.message.channel.create_webhook(name="sètebot")
                await webhook.send(content="<:tph:833842597679857675> | Vous avez récupéré un TPH, faites `!tph frequency` pour l'allumer", username=wh.name, avatar_url=wh.link)
            elif Checkers(self.message.author.id).tph():
                return await self.error("Vous avez déjà un TPH.")
            else:
                return await self.error("Il n'y a aucun tph à récupérer ici.")
        else:
            return self.error()

            
    async def error(self, msg="Une erreur est survenue"):
        msg = await self.message.channel.send(msg)
        await __import__("asyncio").sleep(5)
        await msg.delete()
        await self.message.delete()
        return None