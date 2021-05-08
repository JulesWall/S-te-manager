
import discord

from db.function.Tph import *
from db.function.WhInit import *
from db.function.ExistProfil import *
from db.files.data import galonDB
from db.function.ExistWh import *
from classes.checkers import *
from db.function.Frequency import *
class Tph():

    def __init__(self, message:discord.Message, bot:discord.Client()):

        self.bot = bot
        self.message = message

    async def run(self):
        try: command = self.message.content.split(" ")[1]
        except : return self.error()
        has_tph = Checkers(self.message.author.id).tph()

        if (command == "take" or command == "t"):
            if self.message.channel.id == 705094420843724870 and not has_tph:
                tph = TphInit(self.message.author.id, int(__import__("time").time()+60*60), "off")
                WhInit(f"tph-{self.message.author.id}",f"tph-{self.message.author.display_name}", str(galonDB[ExistProfil(tph.id_owner).grade]))
                wh = ExistWh(f"tph-{self.message.author.id}")
                try: webhooks = await self.message.channel.webhooks();webhook = webhooks[0]
                except Exception as e: webhook = await self.message.channel.create_webhook(name="sètebot")
                await webhook.send(content=f"**Récupère un tph**", username=self.message.author.display_name, avatar_url=self.message.author.avatar_url)
                await webhook.send(content="(<:tph:833842597679857675> | Vous avez récupéré un TPH, faites `!tph frequency` pour l'allumer)", username=wh.name, avatar_url=wh.link)
            elif Checkers(self.message.author.id).tph():
                return await self.error("Vous avez déjà un TPH.")
            else:
                return await self.error("Il n'y a aucun tph à récupérer ici.")
            await self.message.delete()
        
        elif (command == "speak" or command == "s") and has_tph:
            if self.message.channel.id != ExistProfil(self.message.author.id).location:
                return await self.error("Vous n'êtes pas dans le bon salon.")
            tph = ExistTph(self.message.author.id)
            if tph.frequency == "off":
                return await self.error("Votre tph est éteint.")
            chanfq = Frequency(tph.frequency).convertChannelsStringToChannelList().searchTph()
            chan_list = chanfq.channels 
            transmission = ' '.join(self.message.content.split(' ')[2:])
            for chan in chan_list:
                if chan != self.message.channel.id:
                    wh = ExistWh(f"tph-{self.message.author.id}")
                    try: webhooks = await self.message.guild.get_channel(chan).webhooks();webhook = webhooks[0]
                    except Exception as e: webhook = await self.message.guild.get_channel(chan).create_webhook(name="sètebot")
                    await webhook.send(content=f"__**{tph.frequency}**__ | {transmission} ", username=wh.name, avatar_url=wh.link)
            webhooks = await self.message.channel.webhooks();webhook = webhooks[0]
            await webhook.send(content=f"**Se saisit de son tph et transmet un message** {transmission}", username=self.message.author.display_name, avatar_url=self.message.author.avatar_url)
            await self.message.delete()
            tph.refresh()
        
        elif (command == "drop" or command == "d") and has_tph:
            if self.message.channel.id == 705094420843724870:
                tph = ExistTph(self.message.author.id)
                tph.drop()
                ExistWh(f"tph-{self.message.author.id}").delete()
                try: webhooks = await self.message.channel.webhooks();webhook = webhooks[0]
                except Exception as e: webhook = await self.message.channel.create_webhook(name="sètebot")
                await webhook.send(content=f"**Repose son tph et le mets en charge**", username=self.message.author.display_name, avatar_url=self.message.author.avatar_url)                      
                await self.message.delete()
            else:
                return await self.error("Vous ne pouvez pas poser votre terminal ici.")

        elif (command == "frequency" or command == "f") and has_tph:
            try: frequency = self.message.content.split(" ")[2]
            except: return await self.error()
            try: assert frequency in frequencypossibilities()
            except: return await self.error(f"Fréquence introuvable, voici la liste des fréquences : {frequencypossibilities()}")

            tph = ExistTph(self.message.author.id)
            tph.set_frequency(frequency)
            try: webhooks = await self.message.channel.webhooks();webhook = webhooks[0]
            except Exception as e: webhook = await self.message.channel.create_webhook(name="sètebot")
            await webhook.send(content=f"**Change la fréquence de son tph sur {frequency} **", username=self.message.author.display_name, avatar_url=self.message.author.avatar_url)                      
            await self.message.delete()

        else:
            return await self.error()

            
    async def error(self, msg="Une erreur est survenue"):
        msg = await self.message.channel.send(msg)
        await __import__("asyncio").sleep(5)
        await msg.delete()
        await self.message.delete()
        return None

        