#
#    Sète bot Version 1.1.0 
#

import discord
from Discord.MessageManager import *
from config import *

from Game.Syno.loopsyno import *
from Discord.loop.loop import *

client = discord.Client()
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 
    if IS_MAINTENANCE :
        game = discord.Game("Maintenance en cours !")
        await client.change_presence(status=discord.Status.dnd, activity=game)        
    print("presence set")
    client.loop.create_task(LoopSyno(client).loop())
    client.loop.create_task(RLoop(client).loop())
    print("loopes started")

@client.event
async def on_member_join(member):
    if member.guild.id == 705059899750613013:
        await member.add_roles(member.guild.get_role(836026069991424070))

@client.event
async def on_message_edit(before, after): 
    await on_message(after)
    log = client.get_guild(705059899750613013).get_channel(836277984486621194)
    embed=discord.Embed(color=0xff6f00)
    string = f":wrench: __**Info**__ \n**User** : {after.author.id}, <@{after.author.id}>\n **Channel** : <#{after.channel.id}>\n\n :page_facing_up:  **Message avant**:```{before.content}```\n :page_with_curl:  **Message après**:```{after.content}```"
    embed.add_field(name="Message édité", value=string, inline=False)
    await log.send(embed=embed)  

@client.event
async def on_message_delete(message):
    log = client.get_guild(705059899750613013).get_channel(836277984486621194)
    embed=discord.Embed(color=0xff6f00)
    string = f" :microscope:  __**Info**__ \n**User** : {message.author.id}, <@{message.author.id}>\n **Channel** : <#{message.channel.id}>\n\n :page_facing_up:  **Message supprimé**:```{message.content}```"
    embed.add_field(name="Message supprimé", value=string, inline=False)
    await log.send(embed=embed)

@client.event
async def on_message(message): 
    await MessageManager(message,  client).manage()

client.run(TOKEN)

