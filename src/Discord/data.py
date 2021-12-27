from Discord.command.utility.ping import *
from Discord.command.admin.eval import *
from Discord.command.admin.shutdown import *
from Discord.command.game.profil import *
from Discord.command.game.top import *
from Discord.command.game.pds import *
from Discord.command.game.disponible import *
from Discord.command.game.statut import *
from Discord.command.game.wh import *
from Discord.command.game.tph import *
from Discord.command.game.mdj import *
from Discord.command.game.intervention import *
from Discord.command.game.house import *
from Discord.command.game.bip import *
from Discord.command.admin.forceservice import *

commands = {
    "ping":[Ping],
    "eval":[Eval],
    "shutdown":[ShutDown],
    "profil":[Profil],
    "top":[Top],
    "pds":[Pds],
    "fds":[Pds],
    "disponible":[Dispo],
    "statut":[Statut],
    "wh":[wh],
    "tph":[Tph],
    "mdj":[Mdj],
    "intervention":[Intervention],
    "house":[House],
    "forceservice":[ForceService],
    "bip":[Bip]
}

rp_categories = [
    836028546618490931, #🚒 Centre de Secours
    836041990142951424, #🌐 Lieux
    705087219592986735, #34200 | Ville de Sète
    705089353990275183, #34110 | Ville de Frontignan
    705089462576873622, #34540 | Balaruc-les-Bains
    705090448385114132, #34540 | Balaruc-le-Vieux
    705090482891653181, #34140 | Ville de Bouzigues
    705090522401865769, #34560 | Ville de Poussan
    836028397880606760 #🏢 Appartements
]
