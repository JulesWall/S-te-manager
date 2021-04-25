import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

from db.function.Querry import Querry
from db.files.data import *
from db.function.ExistProfil import ExistProfil

class BipInit():

    def __init__(self, id_owner, expiration):

        self.id_owner = id_owner
        self.expiration = expiration
        
        Querry(f"INSERT INTO `bip`(`id_owner`, `expiration`)\
        VALUES ({self.id_owner},{self.expiration})")

class ExistTph():

    def __init__(self, id_owner):
        data = Querry(f"SELECT * FROM `bip` WHERE `id_owner`='{id_owner}'")
        id, self.id_owner, self.expiration = data[0]
        self.channel = ExistProfil(self.id_owner).location
    
    def drop(self):
        Querry(f"DELETE from bip WHERE `id_owner`={self.id_owner}")

    def has_expired(self):
        return __import__("time").time() > self.expiration

async def expired_pager_manager():
    try:
        datas = Querry("SELECT * FROM bip")
        for data in datas:
            bip = ExistBip(wh[1])
            if bip.has_expired() and not bip.has_low_battery:
                bip.set_lowbattery()
                bip.set_time_before_down()
                
            elif bip.has_expired and bip.has_low_battery:
                ExistProfil(bip.id_owner).end_service()
                bip.drop()
            
    except: pass


