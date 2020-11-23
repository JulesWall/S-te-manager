import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

def NewWebhook(alias, pseudo, url):
    db = MySQLdb.connect(user=USERDATABASE, passwd=PASSWORDDATABASE, host="localhost", db=DATABASE)
    cursor = db.cursor()
    sql = f'INSERT INTO `webhook`(`alias`, `pseudo`, `url`) VALUES ({alias},{pseudo},{url})'
    cursor.execute(sql) 
    db.commit()
    db.close()

def ExistWebhook(alias):
    db = MySQLdb.connect(user=USERDATABASE, passwd=PASSWORDDATABASE, host="localhost", db=DATABASE)
    cursor, sql = db.cursor(), str(sql)
    cursor.execute(f"SELECT `alias`, `pseudo`, `url` FROM `webhook` WHERE `alias`='{alias}'")
    data = cursor.fetchall()
    db.close()
    return data