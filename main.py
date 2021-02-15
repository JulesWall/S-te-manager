import discord
from Engine import *
from config import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))   

@client.event
async def on_message_edit(before, after): await on_message(after)   
    
@client.event
async def on_message(message): await Engine(message, client).run()

client.run(TOKEN)
