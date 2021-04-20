#
#    Sète bot Version 1.0
#
import discord
from Engine import *
from config import *

from Syno.loopsyno import *
from db.function.ExistWh import delete_expired_wh

client = discord.Client()
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 
    client.loop.create_task(LoopSyno(client).loop())
    delete_expired_wh()

@client.event
async def on_message_edit(before, after): await on_message(after)   
    
@client.event
async def on_message(message): await Engine(message,  client).run()

client.run(TOKEN)

