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

commands = {
    "ping":[Ping],
    "p":[Ping],
    "eval":[Eval],
    "e":[Eval],
    "shutdown":[ShutDown],
    "profil":[Profil],
    "top":[Top],
    "pds":[Pds],
    "fds":[Pds],
    "disponible":[Dispo],
    "statut":[Statut],
    "wh":[wh],
    "tph":[Tph],
    "mdj":[Mdj]
}

