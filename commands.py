from command.utility.ping import *
from command.admin.eval import *
from command.admin.shutdown import *
from command.game.profil import *
from command.game.top import *
from command.game.pds import *
from command.game.disponible import *
from command.game.statut import *
from command.game.wh import *
from command.game.tph import *

commands = {
    "ping":[Ping],
    "p":[Ping],
    "eval":[Eval],
    "e":[Eval],
    "shutdown":[ShutDown],
    "profil":[Profil],
    "top":[Top],
    "pds":[Pds],
    "disponible":[Dispo],
    "statut":[Statut],
    "wh":[wh],
    "tph":[Tph]
}

