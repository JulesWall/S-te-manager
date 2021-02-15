import discord
from config import *

from function.checkers import *
from function.getters import *

from db.function.ProfilInit import *
from db.function.ExistProfil import *

from db.files.data import *

class Profil():

    def __init__(self, message:discord.Message, bot:discord.Client()):
        
        self.message = message
        self.bot = bot

    async def run(self):
        getter = Getters(self.message, self.bot)
        idd = getter.id 
        name = getter.get_name()
        grade = getter.get_grade()
        init = ProfilInit(idd, name, grade)

        data = ExistProfil(getter.id)
        embed=discord.Embed(title="Profil", color=0xff0000)
        embed.add_field(name="Nom:", value=f"{data.name}", inline=False)
        embed.add_field(name="Grade:", value=f"{gradeDB[data.grade]}", inline=False)
        embed.add_field(name="Argent:", value=f"{data.money} €", inline=False)
        embed.add_field(name="Condition Physique", value=f"{data.CP} %", inline=False)     
        embed.set_thumbnail(url=f"{galonDB[data.grade]}")
        await self.message.channel.send(embed=embed)
        return None
