from db.function.Querry import Querry
from db.files.data import *
import time

class ExistWh():

    def __init__(self, alias):
        data = Querry(f"SELECT * FROM `wh` WHERE `alias`='{alias}'")
        id, self.alias, self.name, self.link, self.lastuse = data[0]
        self.expiration_str = time.ctime(self.lastuse + 2_592_000)
    
    def has_expired(self):
        self.expired_time = self.lastuse + 2_592_000 #1 mois
        return __import__("time").time() > self.expired_time
    
    def delete(self):
        Querry(f"DELETE FROM wh WHERE `name`='{self.name}'")
          
    def update_lastuse(self):
        self.lastuse = __import__("time").time()
        Querry(f"UPDATE wh SET `lastuse`={self.lastuse} WHERE `name`='{self.name}'")
    
def delete_expired_wh():
    try:
        whs = Querry("SELECT name FROM wh")
        for wh in whs:
            whh = ExistWh(wh[0])
            if whh.has_expired():
                whh.delete()
    except : pass