import discord
import time
import os

from Discord.command.Command import *
from db.Player.checkers import *

class Restart(CtaCommand):

    def __init__(self, message, bot):
        CtaCommand.__init__(self, message, bot)

    async def run(self):
        if not self.has_permission : return await self.not_permission()

        with open("restart.txt", 'r') as file:
            last_use = float(file.read().strip())  # Lire le dernier temps enregistré
    
        if time.time() - last_use >= 300:
            self.message.channel.send("Redémarrage du bot !")
            with open("restart.txt", 'w') as file:
                file.write(str(time.time()))
            os.system("pm2 restart all")
        
        else : self.message.channel.send("Le bot a déja été redémarré il y a moins de 5 minutes.")

            
