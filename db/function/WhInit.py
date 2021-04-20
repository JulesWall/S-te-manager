import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *
import time

from db.function.Querry import Querry
from db.files.data import *


class WhInit():

    def __init__(self, name, link):

        self.name = name
        self.link = link
        self.time = time.time()

        Querry(f"DELETE FROM `wh` WHERE `name`='{self.name}'")
        Querry(f"INSERT INTO `wh` (`name`, `link`, `lastuse`) VALUES ('{self.name}','{self.link}',{self.time})")



