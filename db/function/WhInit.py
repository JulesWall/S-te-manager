import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *
import time

from db.function.Querry import Querry
from db.files.data import *


class WhInit():

    def __init__(self, alias, name, link):

        self.alias = alias
        self.name = name
        self.link = link
        self.time = time.time()

        Querry(f"DELETE FROM `wh` WHERE `alias`='{self.alias}'")
        Querry(f"INSERT INTO `wh` (`alias`, `name`, `link`, `lastuse`) VALUES ('{self.alias}','{self.name}','{self.link}',{self.time})")



