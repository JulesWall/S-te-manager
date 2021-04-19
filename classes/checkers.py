import discord

from db.files.data import *
from db.function.Querry import *

class Checkers():

    def __init__(self, id):

        self.id = id
       # self.member = self.server.get_member(int(self.id))

    def player(self):
        if len(Querry(f"SELECT * FROM `profil` WHERE `idd`={int(self.id)}")) == 0: return False
        else : return True
    
    def astreinte(self):
        if len(Querry(f"SELECT * FROM `service` WHERE `idd`={int(self.id)}")) == 0: return False
        else : return True
    
    def cta(self):
        poste = Querry(f"SELECT poste FROM `profil` WHERE `idd`={int(self.id)}")
        if len(poste) == 0: return False
        try:
            if '5' in str(poste[0][0]) : return True
            else : return False
        except: return False