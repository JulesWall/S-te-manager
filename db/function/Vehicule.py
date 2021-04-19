import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

from db.function.Querry import Querry
from db.files.data import *

class Vehicule():

    def __init__(self, name):
        data = Querry(f"SELECT * FROM `vhl` WHERE `véhicule`='{name}'")
        #`id`, `statut`, `véhicule`, `cord`, `syno`, `required`
        id, self.statut, self.vehicule, self.cord, self.syno, self.required, self.calculator = data[0]
    
    def save(self):
        data = Querry(f"UPDATE `vhl` SET `statut`={self.statut} WHERE `véhicule`='{self.vehicule}'")

def get_all_vehicule(): return Querry("SELECT véhicule FROM vhl")