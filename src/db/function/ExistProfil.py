import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

from db.function.Querry import Querry
from db.files.data import *

class ExistProfil():

    def __init__(self, idd):

        data = Querry(f"SELECT * FROM `profil` WHERE idd={idd}")
        id, self.idd, self.name, self.grade, self.hierarchie, self.poste, self.money, self.CP, self.location, self.service_time, self.intervention = data[0]
            
    def start_service(self, cta):
        astreinte = Querry(f"INSERT INTO `service`(`idd`, `name`, `time`, `cta`)\
        VALUES ({self.idd},'{self.name}',{__import__('time').time()},{cta})")

    def end_service(self):
        time = Querry(f"SELECT `time` FROM service WHERE idd={self.idd}")
        end = Querry(f"DELETE FROM `service` WHERE idd={self.idd}")
        return time[0][0]

    def update_cp(self, value):
        try : assert self.CP+value > 0
        except : self.CP, value = 0,0
        uptade = Querry(f"UPDATE `profil` SET `CP`={self.CP+value} WHERE idd={self.idd}")
        return value
        
    def update_money(self, value):
        uptade = Querry(f"UPDATE `profil` SET `money`={self.money+value} WHERE idd={self.idd}")
        return value

    def update_location(self, value):
        self.location = value
        uptade = Querry(f"UPDATE `profil` SET `location`={self.location} WHERE idd={self.idd}")
        return value
    
    def add_service_time(self, value):
        self.service_time += value
        uptade = Querry(f"UPDATE `profil` SET `service_time`={self.service_time} WHERE idd={self.idd}")
        return value


        
    
    