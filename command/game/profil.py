import discord
from config import *

from classes.checkers import *
from classes.getters import *

from db.function.ProfilInit import *
from db.function.ExistProfil import *

from db.files.data import *

class Profil():

    def __init__(self, message:discord.Message, bot:discord.Client()):
        
        self.message = message
        self.bot = bot

    async def run(self):
        
        if Checkers(self.message.author.id).player(): await self.update()
        else: await self.init()

    async def init(self):
        getter = Getters(self.message, self.bot)
        idd = getter.id 
        name = getter.get_name()
        grade = getter.get_grade()
        poste = getter.get_poste()
        init = ProfilInit(idd, name, grade, poste)
        await self.show()
       
    async def update(self):
        getter = Getters(self.message, self.bot)
        idd = getter.id 
        name = getter.get_name()
        grade = getter.get_grade()
        poste = getter.get_poste()
        data = ExistProfil(getter.id)
        init = ProfilInit(idd, name, grade, poste, data.money, data.CP)
        await self.show()

    async def show(self):
        getter = Getters(self.message, self.bot)
        data = ExistProfil(getter.id)
        self.string = ''
        for poste in data.poste: 
            try: self.string += f"{postedb[int(poste)]}\n"
            except:continue
        embed=discord.Embed(title="Profil", color=0xff0000)
        embed.add_field(name="Nom:", value=f"{data.name}", inline=False)
        embed.add_field(name="Grade:", value=f"{gradeDB[data.grade]}", inline=False)
        if self.string != '':
            embed.add_field(name="Poste:", value=f"{self.string}", inline=False)
        embed.add_field(name="Argent:", value=f"{data.money} €", inline=False)
        embed.add_field(name="Condition Physique", value=f"{data.CP} %", inline=False)     
        embed.set_thumbnail(url=f"{galonDB[data.grade]}")
        embed.set_footer(text=FOOTER)
        await self.message.channel.send(embed=embed)