import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

from db.function.Querry import Querry
from db.files.data import *

class ProfilInit():

    def __init__(self, idd, name, grade):

        self.name = name
        self.idd = idd
        self.grade = grade
        print(self.grade)
        self.hierarchie = hierarchieDB[self.grade]
        self.money = 0
        self.CP = 100

        Querry(f"DELETE FROM `profil` WHERE `idd`={self.idd}")
        Querry(f"INSERT INTO `profil`(`idd`, `name`, `grade`, `hierarchie`, `money`, `CP`)\
        VALUES ({self.idd},'{self.name}',{self.grade},{self.hierarchie},{self.money},{self.CP})")

