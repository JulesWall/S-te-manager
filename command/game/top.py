import discord 
from db.function.top import get_top
from config import *

class Top():

    def __init__(self, message:discord.Message, bot:discord.Client()):

        self.bot = bot
        self.message = message

    async def run(self):
        top = get_top('money', 'cp')
        string = ''; ii = 0
        for i in top:
            #idd, {0}, {1}, name
            ii += 1; string += f'**#{ii}** | **{i[3]}** : Argent: {i[1]} € Condition physique : {i[2]} %\n'

        embed=discord.Embed(title="Top", description=f"{string}", color=0xff6f00)
        embed.set_footer(text=FOOTER)
        await self.message.channel.send(embed=embed)
