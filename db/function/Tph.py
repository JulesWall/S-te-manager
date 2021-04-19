import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

from db.function.Querry import Querry
from db.files.data import *

class TphInit():

    def __init__(self, id_owner, channel, expiration, frequency):

        self.id_owner = id_owner
        self.channel = channel
        self.expiration = expiration
        self.frequency = frequency

        
        Querry(f"INSERT INTO `tph`(`id_owner`, `channel`, `expiration`, `Frequency`)\
        VALUES ({self.id_owner},'{self.channel}',{self.expiration},'{self.frequency}')")

class ExistTph():

    def __init__(self, id_owner):
        data = Querry(f"SELECT * FROM `tph` WHERE `id_owner`='{id_owner}'")
        id, self.id_owner, self.channel, self.expiration, self.frequency = data[0]
    
    def drop(self):
        Querry(f"DELETE from tph WHERE `id_owner`={self.id_owner}")

    def set_frequency(self, frequency):
        self.frequency = frequency
        Querry(f"UPDATE tph SET `frequency`={self.frequency} WHERE `id_owner`={self.id_owner}")
    
    def refresh(self):
        self.expiration = __import__("time").time() + 60*60
        Querry(f"UPDATE tph SET `expiration`={self.expiration} WHERE `id_owner`={self.id_owner}")

    def has_expired(self):
        return __import__("time").time() > self.expiration



