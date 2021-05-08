import discord

from db.files.data import *

class Getters():

    def __init__(self, message, bot, id=0):

        self.bot = bot
        self.message = message
        self.server = self.message.guild
        if id==0: self.id = self.message.author.id
        else : self.id = id
        self.member = self.server.get_member(int(self.id))
    
    def get_grade(self):
        checklist = []
        for i in self.member.roles: checklist.append(i.id)

        founds = [];maxi = -1
        for i in gradeServeur.keys():
            if i in checklist: founds.append(gradeServeur[i])
        if len(founds) == 0: return None
        else : return max(founds)

    def get_poste(self):
        checklist = []
        for i in self.member.roles: checklist.append(i.id)

        founds = [];maxi = -1
        for i in posteserveur.keys():
            if i in checklist: founds.append(posteserveur[i])
        return tuple(founds)
    
    def get_name(self):
        user_name = self.member.display_name
        try : return str(user_name.split()[1] + ' ' + user_name.split()[2])
        except: return 'undetermined'
    

