from db.function.Querry import Querry
from db.function.ExistProfil import ExistProfil
import discord

class Frequency():

    def __init__(self, fq):
        data = Querry(f"SELECT * FROM `tph_frequency` WHERE `Frequency`='{fq}'")
        id, self.frequency, self.channels = data[0]
    
    def convertChannelsStringToChannelList(self):
        self.channels = self.channels.replace("[", "").replace(']', "").split(",")
        for i in range(len(self.channels)):self.channels[i] = int(self.channels[i])
        return self
    
    def searchTph(self):
        tphs = Querry(f"SELECT id_owner FROM tph WHERE `Frequency`='{self.frequency}'")
        for tph in tphs: self.channels.append(ExistProfil(tph[0]).location)
        return self
    
def frequencypossibilities():
    possibilities = []
    for f in Querry("SELECT Frequency from `tph_frequency`"):
        possibilities.append(f[0])
    return possibilities


    