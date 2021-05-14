from config import FOOTER
import json
import discord

class InterventionInit():

    def __init__(self, dictionary):
        self.path = "/Users/Juels/Desktop/Github/csp/src/Game/Intervention/interventions.json"

        with open(self.path, "r") as f:
            self.interventions = json.load(f)
        self.num = __import__("random").randint(111111, 999999)

        self.interventions[self.num] = dictionary

        with open(self.path, "w") as f:
            json.dump(self.interventions, f)

class ExistIntervention():

    def __init__(self, num):
        self.path = "/Users/Juels/Desktop/Github/csp/src/Game/Intervention/interventions.json"

        with open(self.path, "r") as f:
            interventions = json.load(f)

        self.num = num    
        self.intervention = interventions[self.num]
        self.code_inter = self.intervention["code_intervention"]
        self.motif = self.intervention["motif"]
        self.adresse = self.intervention["adresse"]
        self.moyens = self.intervention["moyens"]
        self.details = self.intervention["details"]
        self.to_alert = self.intervention["to_alert"]
    
    def cembed(self):

        embed_ticket=discord.Embed(
            title=f"Feuille de départ N°{self.num}",
            description=f"**CODE INTERVENTION** | **{self.code_inter}**",
            color=0xfbff00)
        embed_ticket.add_field(name="Motif du départ:", value=self.motif, inline=False)
        embed_ticket.add_field(name="Détails de l'intervention:", value=self.details, inline=False)
        embed_ticket.add_field(name="Adresse de l'intervention:", value=self.adresse, inline=False)
        embed_ticket.add_field(name="Moyens engagés:", value=self.moyens, inline=False)
        embed_ticket.set_footer(text=FOOTER)
        self.embed_ticket = embed_ticket

        will_alerted = "**Les personnels suivant seront alertés :**\n"
        for uid in self.to_alert:
            will_alerted += f"\n - <@{uid}>"
        will_alerted += "\n\nAppuyez sur la réaction pour déclencher l'alerte."
        self.embed_will_alerted = discord.Embed(description=will_alerted, color=0x00fffb)
