import discord

from Discord.command.Command import *
from Discord.MessageSender import *
from db.function.Tph import *
from db.function.WhInit import *
from db.function.ExistProfil import *
from db.files.data import galonDB
from db.function.ExistWh import *
from db.Player.checkers import *
from db.function.Frequency import *

class Mdj(CtaCommand):

    def __init__(self, message, bot):
        CtaCommand.__init__(self, message, bot)
        self.args1 = {
            "cta":"cta",
            "c15":"c15"
        }

    async def run(self):
        if not self.has_permission : return await self.not_permission()

        try:
            fq = await self.get_args(self.args1, 1)
            chanfq = Frequency(fq).convertChannelsStringToChannelList().searchTph()
            chan_list = chanfq.channels
            transmission = ' '.join(self.message.content.split(' ')[2:])
            assert fq in ["cta", "c15"]
        except:
            return await self.error()

        avna = {"cta":{"name":"CTA-CODIS-34", "avatar":"https://i.servimg.com/u/f32/11/89/35/34/logo_c11.jpg"},
        "c15":{"name":"Centre 15", "avatar":"https://images.midilibre.fr/api/v1/images/view/5b4608153e45464a454a1f4d/large/image.jpg"}
        }
        for chan in chan_list:
            await MessageSender(self.message, self.bot).wh(
                name = avna[fq]["name"],
                avatar_url = avna[fq]["avatar"],
                msg = f"[**{fq}**] > {transmission}",
                channel=self.message.guild.get_channel(chan)
            )
        await self.message.delete()
