
import discord

from Discord.command.Command import *
from db.function.Tph import *
from db.function.WhInit import *
from db.function.ExistProfil import *
from db.files.data import galonDB
from db.function.ExistWh import *
from db.Player.checkers import *
from db.function.Frequency import *

class Tph(GameCommand):

    def __init__(self, message, bot):
        GameCommand.__init__(self, message, bot)
        self.args1 = {
            "take":self.take,
            "drop":self.drop,
            "speak":self.speak,
            "frequency":self.frequency
        }

    async def run(self):
        if not self.has_permission : return await self.not_permission()
        
        self.has_tph = Checkers(self.message.author.id).own_tph()

        try:
            arg = await self.get_args(self.args1, 1) 
            assert arg != None
        except: 
            await self.error()
            return None        
        await arg()

    async def take(self):
        if self.message.channel.id == 705094420843724870 and not self.has_tph:
            tph = TphInit(self.message.author.id, int(__import__("time").time()+60*60), "off")
            WhInit(f"tph-{self.message.author.id}",f"tph-{self.message.author.display_name}", str(galonDB[ExistProfil(tph.id_owner).grade]))
            wh = ExistWh(f"tph-{self.message.author.id}")
            ms = MessageSender(self.message, self.bot)
            await ms.wh(
                name = self.message.author.display_name,
                avatar_url=self.message.author.avatar_url,
                msg = "**Récupère un tph**"
            )
            await ms.wh(
                name = wh.name,
                avatar_url=wh.link,
                msg = "<:tph:833842597679857675> | Vous avez récupéré un TPH, faites `!tph frequency` pour l'allumer"
            )
        elif self.has_tph:
            return await self.error("Vous avez déjà un TPH.")
        else:
            return await self.error("Il n'y a aucun tph à récupérer ici.")
        await self.message.delete()

    async def drop(self):
        if self.message.channel.id == 705094420843724870:
            tph = ExistTph(self.message.author.id)
            tph.drop()
            await MessageSender(self.message, self.bot).wh(
                name = self.message.author.display_name,
                avatar_url=self.message.author.avatar_url,
                msg = "**Repose son tph et le mets en charge**"
            )
            await self.message.delete()
        else:
            return await self.error("Vous ne pouvez pas poser votre terminal ici.")

    async def speak(self):
        if self.message.channel.id != ExistProfil(self.message.author.id).location:
            return await self.error("Vous n'êtes pas dans le bon salon.")
        tph = ExistTph(self.message.author.id)
        if tph.frequency == "off":
            return await self.error("Votre tph est éteint.")
        chanfq = Frequency(tph.frequency).convertChannelsStringToChannelList().searchTph()
        chan_list = chanfq.channels
        chan_list.remove(self.message.channel.id)
        transmission = ' '.join(self.message.content.split(' ')[2:])
        for chan in chan_list:
            wh = ExistWh(f"tph-{self.message.author.id}")
            await MessageSender(self.message, self.bot).wh(
            name = wh.name,
            avatar_url = wh.link,
            msg = f"[**{tph.frequency}**] > {transmission}",
            channel=self.message.guild.get_channel(int(chan))
            )

        await self.message.delete()

        await MessageSender(self.message, self.bot).wh(
                name = self.message.author.display_name,
                avatar_url=self.message.author.avatar_url,
                msg = f"**Se saisit de son tph et transmet un message** {transmission}"
            )

        tph.refresh()

    async def frequency(self):
        try: frequency = self.message.content.split(" ")[2]
        except: return await self.error()
        try: assert frequency in frequencypossibilities()
        except: return await self.error(f"Fréquence introuvable, voici la liste des fréquences : {frequencypossibilities()}")

        tph = ExistTph(self.message.author.id)
        tph.set_frequency(frequency)
        await MessageSender(self.message, self.bot).wh(
                name = self.message.author.display_name,
                avatar_url=self.message.author.avatar_url,
                msg = f"**Change la fréquence de son tph sur {frequency} **"
            )
        
        await self.message.delete()