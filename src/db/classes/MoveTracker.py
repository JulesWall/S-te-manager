import discord

from db.function.Tph import ExistTph
from db.function.ExistProfil import ExistProfil
from db.Player.checkers import *

class MoveTracker():

    def __init__(self, message, bot):
        self.bot = bot
        self.message = message
        self.channel = message.channel
        self.rp_categories = [705086857666625556, 705087129230901308, 705087219592986735, 705089353990275183, 705089462576873622, 705090448385114132, 705090522401865769, 708006905741574168]
        self.player = ExistProfil(self.message.author.id)

    def hasMove(self):
        self.oldchan = self.player.location
        self.newchan = self.channel
        return self.oldchan != self.newchan.id

    async def move(self):      
        self.player.update_location(self.newchan.id)
        await on_move(self.oldchan, self.newchan)
        return await self.log()
    
    async def log(self):
        await self.message.guild.get_channel(705079279100362912).send(f"{self.message.author.display_name} s'est déplacé de <#{self.oldchan}> vers <#{self.newchan.id}>")
        return 'logged'


async def on_move(oldchan, newchan):
    pass
    

