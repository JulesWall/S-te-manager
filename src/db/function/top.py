import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

from db.function.Querry import Querry
from db.files.data import *

def get_top(argument, second):
    db = MySQLdb.connect(user=USERDATABASE, passwd=PASSWORDDATABASE, host="localhost", db=DATABASE, charset='utf8mb4')
    cursor = db.cursor()
    cursor.execute("SELECT idd, {0}, {1}, name FROM profil ORDER BY {0} DESC, {1} DESC".format(argument, second))
    data = cursor.fetchall()
    return data
    db.close()

    