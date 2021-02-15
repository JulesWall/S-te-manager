from command.utility.ping import *
from command.admin.eval import *
from command.admin.shutdown import *
from command.game.profil import *

commands = {
    "ping":[Ping],
    "p":[Ping],
    "eval":[Eval],
    "e":[Eval],
    "shutdown":[ShutDown],
    "profil":[Profil]
}

