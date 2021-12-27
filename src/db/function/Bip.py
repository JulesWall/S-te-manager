from db.function.Querry import Querry
from db.files.data import *
from db.function.ExistProfil import ExistProfil

class BipInit():

    def __init__(self, id_owner, statut):

        self.id_owner = id_owner
        self.statut = statut
        
        Querry(f"INSERT INTO `bip`(`id_owner`, `statut`)\
        VALUES ({self.id_owner},'{self.statut}')")

class ExistBip():

    def __init__(self, id_owner):
        data = Querry(f"SELECT * FROM `bip` WHERE `id_owner`='{id_owner}'")
        id, self.id_owner, self.statut = data[0]
        self.channel = ExistProfil(self.id_owner).location
    
    def update(self, statut):
        has_change = self.statut == statut
        self.statut = statut
        update = Querry(f"UPDATE `bip` SET `Statut`='{self.statut}' WHERE `id_owner`='{self.id_owner}'")
        return has_change



