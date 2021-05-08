import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

def Querry(sql):
    db = MySQLdb.connect(user=USERDATABASE, passwd=PASSWORDDATABASE, host="localhost", db=DATABASE)
    cursor, sql = db.cursor(), str(sql)
    cursor.execute(sql) 
    db.commit()
    data = cursor.fetchall()
    db.close()
    return data