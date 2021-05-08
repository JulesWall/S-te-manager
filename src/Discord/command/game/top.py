import discord 
from db.function.top import get_top
from config import *

class Top():

    def __init__(self, message:discord.Message, bot:discord.Client()):

        self.bot = bot
        self.message = message

    async def run(self):
        top = get_top('service_time', 'cp')
        string = ''; ii = 0; limit = 15
        for i in top:
            #idd, {0}, {1}, name
            days = int((i[1]/60)/24)
            hours = int((i[1]/60) - days*24)
            minutes = int(i[1] - (hours*60+days*24*60))
            ii += 1; string += f'**#{ii}** | **{i[3]}** : Temps de service : `{days} jour(s), {hours} heure(s) et {minutes} minute(s)`\n'
            if ii>limit:break

        embed=discord.Embed(title="Top", description=f"{string}", color=0xff6f00)
        embed.set_footer(text=FOOTER)
        await self.message.channel.send(embed=embed)
