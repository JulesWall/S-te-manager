import discord 
from db.function.Webhook import *

class CWebhook():

    def __init__(self, message, bot):
        self.message = message
        self.channel = message.channel
        self.bot = bot
    
    async def run(self):
        msg = self.message.content.split("")
        if len(self.channel.webhooks) == 0:

        if msg[1].startswith("n"):
            msg2 = self.message.content.split("|")
            alias, pseudo, url = msg2[1], msg[2], msg[3]
            NewWebhook(alias, pseudo, url)
            await self.channel.send("added")
