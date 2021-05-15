import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

from db.function.Querry import Querry
from db.files.data import *
from db.function.ExistProfil import ExistProfil

class TphInit():

    def __init__(self, id_owner, expiration, frequency):

        self.id_owner = id_owner
        self.expiration = expiration
        self.frequency = frequency
        
        Querry(f"INSERT INTO `tph`(`id_owner`, `expiration`, `Frequency`)\
        VALUES ({self.id_owner},{self.expiration},'{self.frequency}')")

class ExistTph():

    def __init__(self, id_owner):
        data = Querry(f"SELECT * FROM `tph` WHERE `id_owner`='{id_owner}'")
        id, self.id_owner, self.expiration, self.frequency = data[0]
        self.channel = ExistProfil(self.id_owner).location
    
    def drop(self):
        Querry(f"DELETE from tph WHERE `id_owner`={self.id_owner}")
        alias = "tph-" +str(self.id_owner)
        Querry(f"DELETE from wh WHERE alias={alias}")

    def set_frequency(self, frequency):
        self.frequency = frequency
        Querry(f"UPDATE tph SET `frequency`='{self.frequency}' WHERE `id_owner`={self.id_owner}")
    
    def refresh(self):
        self.expiration = __import__("time").time() + 60*60*1.5
        Querry(f"UPDATE tph SET `expiration`={self.expiration} WHERE `id_owner`={self.id_owner}")

    def has_expired(self):
        return __import__("time").time() > self.expiration

def delete_expired_tph():
    try:
        whs = Querry("SELECT * FROM tph")
        for wh in whs:
            tph = ExistTph(wh[1])
            if tph.has_expired():
                tph.drop()
    except: pass
