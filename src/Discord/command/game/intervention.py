import discord
from Discord.command.Command import *
from db.function.ExistWh import *
from Game.Intervention.Intervention import *
from Discord.MessageSender import *

class Intervention(CtaCommand):

    def __init__(self, message, bot):
        CtaCommand.__init__(self, message, bot)
        self.args1 = {
            "new":self.create(),
            "create":self.create(),
            "alert":self.alert()
        }
        
    async def run(self):
        if not self.has_permission : return await self.not_permission() 

        #try:
        arg = await self.get_args(self.args1, 1) 
        assert arg != None
        #except: 
         #   await self.error()
          #  return None        
        await arg

    async def create(self):
        intervention = {}

        def check(m):
            return m.author == self.message.author and m.channel == self.channel

        await self.channel.send("**Interfaces de création d'intervention:**")

        ask = [
            "> Code d'intervention ?",
            "> Motif d'intervention ?",
            "> Adresse de l'intervention ?",
            "> Moyens engagés ?",
            "> Informations complémentaires ?"
        ]

        answer = [
            "__Code d'intervention :__ {}",
            "__Motif d'intervention :__ {}",
            "__Adresse de l'intervention :__ {}",
            "__Moyens engagés :__ {}",
            "__Informations complémentaires :__ {}"
        ]

        arg = [
            "code_intervention",
            "motif",
            "adresse",
            "moyens",
            "details"
        ]

        for i in range(len(ask)):
            await self.channel.send(ask[i])
            msg = await self.bot.wait_for('message', check=check)
            await self.channel.send(answer[i].format(msg.content))
            intervention[arg[i]] = msg.content
         
        await self.channel.send("Quelles sont les personnes à alerter pour cette intervention ?\n > Merci de transmettre les identifiants discord \nex: `381116968327053313 301027830509207554`")
        msg = await self.bot.wait_for('message', check=check)
        intervention["to_alert"] = []
        for uid in msg.content.split():
            try:
                uid = int(uid)
                intervention["to_alert"].append(uid)
            except:
                pass
        
        await self.channel.send(f"Intervention enregistrée sous le numéro : {InterventionInit(intervention).num}")

    async def delete(self):
        try:
            inter = int(self.message.content.split()[2])
        except:
            return await self.error()
        

    async def alert(self):
        #try:
        intervention = ExistIntervention(self.message.content.split()[2])
        intervention.cembed()
        #except:
         #   return None
        
        await self.channel.send(embed=intervention.embed_ticket)
        msg = await self.channel.send(embed=intervention.embed_will_alerted)
        await msg.add_reaction("✅")

        def check(reaction, user):
            return user == self.message.author and str(reaction.emoji) == '✅'

        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

        
        ville = {
            "s":705087219592986735,
            "f":705089353990275183,
            "bb":705089462576873622,
            "bv":705090448385114132,
            "b":705090482891653181,
            "p":705090522401865769
        }

        def check(m):
            return m.author == self.message.author and m.channel == self.channel

        await self.channel.send("Sur quelle ville est l'intervention ?")
        msg = await self.bot.wait_for('message', check=check)
        print(str(msg.content[0].lower()))
        
        cat = discord.utils.get(self.message.guild.categories, id=int(ville[str(msg.content[0].lower())]))

        await self.message.guild.create_text_channel(
            f"{intervention.num}-{intervention.motif}",
            category=cat
            )
        
        for uid in intervention.to_alert:
            try:
                player = self.message.guild.get_member(uid)
                await player.add_roles(self.message.guild.get_role(705542846035263500))
                u = self.bot.get_user(uid)
                await u.send(f"Vous êtes alerté sur l'intervention {intervention.num}")
            except:
                pass

        await self.message.guild.get_channel(705094420843724870).send(embed=intervention.embed_ticket)
        wh = ExistWh("cta")
        await MessageSender(self.message, self.bot).whe(wh.name, wh.link, intervention.embed_ticket, self.message.guild.get_channel(705094420843724870))
        await MessageSender(self.message, self.bot).wh(wh.name, wh.link, f"<@&705542846035263500>", self.message.guild.get_channel(705094420843724870))
