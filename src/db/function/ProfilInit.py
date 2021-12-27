import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

from db.function.Querry import Querry
from db.files.data import *

class ProfilInit():

    def __init__(self, idd, name, grade, poste, money=0, CP=100, location=782727850624548864, service_time=0):

        self.name = name
        self.idd = idd
        self.grade = grade
        self.poste = str(poste)
        self.hierarchie = hierarchieDB[self.grade]
        self.money = money
        self.CP = CP
        self.location = location
        self.service_time = service_time
        self.intervention = 0

        Querry(f"DELETE FROM `profil` WHERE `idd`={self.idd}")
        Querry(f"INSERT INTO `profil`(`idd`, `name`, `grade`, `hierarchie`, `poste`, `money`, `CP`, `location`, `service_time`, `intervention`)\
        VALUES ({self.idd},'{self.name}',{self.grade},{self.hierarchie},'{self.poste}',{self.money},{self.CP},{self.location},{self.service_time}, {self.intervention})")
        


