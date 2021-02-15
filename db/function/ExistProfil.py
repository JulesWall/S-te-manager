import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

from db.function.Querry import Querry
from db.files.data import *

class ExistProfil():

    def __init__(self, idd):

        data = Querry(f"SELECT * FROM `profil` WHERE idd={idd}")
        #`id`, `idd`, `name`, `grade`, `hierarchie`, `money`, `CP`
        iid, self.idd, self.name, self.grade, self.hierarchie, self.money, self.CP = data[0]
    
    