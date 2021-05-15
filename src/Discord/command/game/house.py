import discord 
import time
from Discord.command.Command import *
from db.Player.checkers import *
from db.function.House import HouseInit

class House(GameCommand):

    def __init__(self, message, bot):
        GameCommand.__init__(self, message, bot)

    async def run(self):
        if not self.has_permission : return await self.not_permission()

        if Checkers(self.message.author.id).own_house:
            await self.channel.send("Vous possédez déjà un appartement.")
        else:
            cat = discord.utils.get(self.message.guild.categories, id=836028397880606760)
            chan = await self.message.guild.create_text_channel(
            f"🏠 Appartement de {self.message.author.display_name}",
            category=cat
            )
            HouseInit(self.message.author.id, int(time.time()+604_800), chan.id)
            await self.channel.send(f"<@{self.message.auhor.id}> | Votre appartement a été créé <#{chan.id}>")

