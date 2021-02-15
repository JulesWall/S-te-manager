import discord

from db.files.data import *
from db.function.Querry import *

class Checkers():

    def __init__(self, id):

        self.id = id
        self.member = self.server.get_member(int(self.id))

    def player(self):
        if len(Querry(f"SELECT * FROM `profil` WHERE `idd`={int(self.id)}")) == 0: return False
        else : return True
    