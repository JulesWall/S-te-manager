from command.utility.ping import *
from command.admin.eval import *
from command.admin.shutdown import *
from command.game.profil import *
from command.game.top import *
from command.game.pds import *

commands = {
    "ping":[Ping],
    "p":[Ping],
    "eval":[Eval],
    "e":[Eval],
    "shutdown":[ShutDown],
    "profil":[Profil],
    "top":[Top],
    "pds":[Pds]
}

