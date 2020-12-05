import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from config import *

def NewWebhook(alias, pseudo, url):
   # try:
    test = ExistWebhook(alias)
    print("ddddddddddddd", test)
    if len(test) == 0:
        db = MySQLdb.connect(user=USERDATABASE, passwd=PASSWORDDATABASE, host="localhost", db=DATABASE)
        cursor = db.cursor()
        sql = f'INSERT INTO `webhooks`(`alias`, `pseudo`, `url pp`) VALUES (\'{alias}\',\'{pseudo}\',\'{url}\')'
        cursor.execute(sql) 
        db.commit()
        db.close()
        return 'added'
    else:
        return 'already exist'
#    except Exception as e: return f'`ERROR`\n{e}'   

def ExistWebhook(alias):
    try:
        db = MySQLdb.connect(user=USERDATABASE, passwd=PASSWORDDATABASE, host="localhost", db=DATABASE)
        cursor= db.cursor()
        cursor.execute(f"SELECT `alias`, `pseudo`, `url pp` FROM `webhooks` WHERE `alias`='{alias}'")
        data = cursor.fetchall()
        db.close()
        return data
    except Exception as e: return f'`ERROR`\n{e}'

def DeleteWebhook(alias):
    try:
        db = MySQLdb.connect(user=USERDATABASE, passwd=PASSWORDDATABASE, host="localhost", db=DATABASE)
        cursor= db.cursor()
        cursor.execute(f"SELECT * FROM `webhooks` WHERE `alias`='{alias}''")
        db.commit
        db.close()
    except Exception as e: return f'`ERROR`\n{e}'