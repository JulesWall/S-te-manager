
import discord
import time

from db.function.Querry import Querry
from db.function.ExistProfil import *
from config import FOOTER

class Dispo():

    def __init__(self, message:discord.Message, bot:discord.Client()):

        self.bot = bot
        self.message = message
        self.player = ExistProfil(self.message.author.id)

    async def run(self):
        datas = Querry("SELECT * FROM service")
        cislist = " "
        ctalist = " "
        for data in datas:
            i, uid, name, starttime, cta = data
            name = self.message.guild.get_member(uid).display_name
            duringtime = time.time() - starttime
            minutes = int(duringtime/60)
            hours = int(minutes/60)
            minutes -= hours*60
            if cta: ctalist += f"- {name} en garde depuis `{hours} heure(s) et {minutes} minute(s)`\n"  
            else : cislist += f"- {name} en garde depuis `{hours} heure(s) et {minutes} minute(s)`\n"  
        
        embedcta = discord.Embed(description=f"{ctalist}", color=0xb3ff00)
        embedcta.set_author(name="Tableau de garde CTA 34", icon_url="https://www.pompiercenter.com/images/sdis/logos/34logo_Logo-Herault-sapeurs-pompiers-rvb-coul%20-%20Copie.jpg")
        embedcta.set_footer(text=FOOTER)

        embedcis = discord.Embed(description=f"{cislist}", color=0xff0000)
        embedcis.set_author(name="Tableau de garde CSP Sète", icon_url="https://www.radioone.fr/upload/news/main/5ec7c8f918faa4.67062370.JPG?=1617323441")
        embedcis.set_footer(text=FOOTER)

        await self.message.channel.send(embed=embedcta)
        await self.message.channel.send(embed=embedcis)