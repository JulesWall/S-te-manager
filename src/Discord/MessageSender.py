import discord

class MessageSender():

    def __init__(self, message, bot):
        self.message = message
        self.bot = bot
        self.channel = message.channel

    async def not_player(self):
        await self.channel.send("Vous devez être un joueur pour exécuter cette commande.")