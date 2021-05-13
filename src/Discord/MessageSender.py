import discord
import json

class MessageSender():

    def __init__(self, message, bot):
        self.message = message
        self.bot = bot
        self.channel = message.channel

    async def not_player(self):
        await self.channel.send(MessageGetter().get("MESSAGE_NOT_PLAYER"))

    async def bot(self, args):
        await self.channel.send(MessageGetter.get(args))
    
    async def embed(self, embed):
        pass

    async def wh(self, name, avatar_url, msg, channel=None):
        if channel == None : channel = self.channel
        try: 
            webhooks = await channel.webhooks();webhook = webhooks[0]
        except Exception as e: 
            webhook = await channel.create_webhook(name="sètebot")
        await self.message.delete()
        await webhook.send(content=msg, username=name, avatar_url=avatar_url)
        
        


class MessageGetter():

    def __init__(self):

        self.file_path = "/Users/Juels/Desktop/Github/csp/src/Message/fr.json"
        self.data = json.loads(self.file_path)
        self.message = "undefined"

    def get(self, cts):

        try: self.message = self.data[cts]
        except: pass
        return self.message



