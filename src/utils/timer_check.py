import discord
import asyncio
from db.function.Querry import *
from db.function.Tph import *
from db.function.Bip import *

def timer_chek(client):
    await delete_expired_tph()
    await expired_pager_manager(client)
