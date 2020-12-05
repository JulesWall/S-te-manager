import discord 
from db.function.Webhook import *

class CWebhook():

    def __init__(self, message, bot):
        self.message = message
        self.channel = message.channel
        self.bot = bot
    
    async def run(self):
        msg = self.message.content.split("|")
        for m in msg: msg[msg.index(m)] = m.replace(" ", "")
       # if len(self.channel.webhooks()) == 0: msg = await self.channel.send("Merci de créer un webhook dans ce salon"); import time; time.sleep(3); await msg.delete(); await self.message.delete()
        if msg[0][-1:].startswith("n"):
            msg2 = self.message.content.split("|")
            alias, pseudo, url = msg2[1], msg2[2], msg2[3]
            await self.message.delete();await self.channel.send(str(NewWebhook(alias, pseudo, url)))
        msg = self.message.content.split()
        if msg[1].startswith('r'):
            await self.channel.send(str(DeleteWebhook(msg[2])))
        elif msg[1].startswith('s'):
            wwh = ExistWebhook(msg[2])[0]
            alias, pseudo, url = wwh[0], wwh[1], wwh[2]
            await self.message.delete()
            webhook = await self.channel.webhooks()
            webhook = webhook[0]
            await webhook.send(content=" ".join(self.message.content.split()[3:]), username=pseudo, avatar_url=url)
        else: pass