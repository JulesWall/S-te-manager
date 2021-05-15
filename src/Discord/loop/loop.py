import discord
import asyncio
import os

from db.function.Tph import *
from db.function.House import *
from db.function.ExistWh import delete_expired_wh

class RLoop():

    def __init__(self, bot):
        self.bot = bot

    async def loop(self):
        while 1:

            delete_expired_tph()
            delete_expired_wh()

            chan_to_delete = delete_expired_house()
            print(chan_to_delete)
            for c in chan_to_delete:
                print('here')
                await self.bot.get_guild(705059899750613013).get_channel(c).delete()

            await asyncio.sleep(200)
