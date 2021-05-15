import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

from db.function.Querry import Querry
from db.files.data import *
from db.function.ExistProfil import ExistProfil

class HouseInit():

    def __init__(self, id_owner, expiration, channel):

        self.id_owner = id_owner
        self.expiration = expiration
        self.channel = channel

        Querry(f"INSERT INTO `House`(`owner_id`, `last_message`, `chan_id`)\
        VALUES ({self.id_owner},{self.expiration},{self.channel})")

class ExistHouse():

    def __init__(self, id_owner):
        data = Querry(f"SELECT * FROM `House` WHERE `owner_id`='{id_owner}'")
        id, self.id_owner, self.expiration, self.channel = data[0]

    def drop(self):
        Querry(f"DELETE from House WHERE `owner_id`={self.id_owner}")
        return self.channel

    def refresh(self):
        self.expiration = __import__("time").time() + 604_800
        Querry(f"UPDATE House SET `last_message`={self.expiration} WHERE `owner_id`={self.id_owner}")

    def has_expired(self):
        return __import__("time").time() > self.expiration

def delete_expired_house():
    supress = []
    try:
        houses = Querry("SELECT * FROM House")
        for house in houses:
            house = ExistHouse(house[1])
            if house.has_expired():
                cid = house.drop()
                supress.append(cid)
    except: pass
    finally: return supress
