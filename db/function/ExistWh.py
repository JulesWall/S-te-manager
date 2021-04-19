from db.function.Querry import Querry
from db.files.data import *

class ExistWh():

    def __init__(self, name):
        data = Querry(f"SELECT * FROM `wh` WHERE `name`='{name}'")
        id, self.name, self.link, self.lastuse = data[0]
    
    def has_expired(self):
        self.expired_time = self.lastuse + 2_592_000 #1 mois
        return __import__("time").time() > self.expired_time
    
    def delete(self):
        Querry(f"DELETE FROM wh WHERE `name`='{self.name}'")
          
    def update_lastuse(self):
        self.lastuse = __import__("time").time()
        Querry(f"UPDATE wh SET `lastuse`={self.lastuse} WHERE `name`='{self.name}'")
    
def delete_expired_wh():
    whs = Querry("SELECT name FROM wh")
    for wh in whs:
        whh = ExistWh(wh[0])
        if whh.has_expired():
            whh.delete()