from command.utility.ping import *
from command.admin.eval import *
from command.admin.shutdown import *

commands = {
    "ping":[Ping],
    "p":[Ping],
    "eval":[Eval],
    "e":[Eval],
    "shutdown":[ShutDown]
}

