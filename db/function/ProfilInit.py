import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

from db.function.Querry import Querry
from db.files.data import *

class ProfilInit():

    def __init__(self, idd, name, grade, poste, money=0, CP=100):

        self.name = name
        self.idd = idd
        self.grade = grade
        self.poste = str(poste)
        self.hierarchie = hierarchieDB[self.grade]
        self.money = money
        self.CP = CP
        self.location = 782727850624548864

        Querry(f"DELETE FROM `profil` WHERE `idd`={self.idd}")
        Querry(f"INSERT INTO `profil`(`idd`, `name`, `grade`, `hierarchie`,  `poste`, `money`, `CP`, `location`)\
        VALUES ({self.idd},'{self.name}',{self.grade},{self.hierarchie},'{self.poste}',{self.money},{self.CP},{self.location})")
        


