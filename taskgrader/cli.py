from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION

from .utils import coloration as clr
from .utils import debug as dbg
from .commands.base import BaseCmd

__doc__ = """
\n
{wrn}{bold}\nTask grader{ec}

This little utils let you test algorithms
by managing the creations of test

Usage:
  taskgrader hello
  taskgrader new
  taskgrader exec <filename> [<stdin>] [<stdout>] [<stderr>]
  taskgrader -h | --help
  taskgrader --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  taskgrader hello
  taskgrader new

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/erik-helmers/grader-cli
"""

# --stdin=<stdin>                   Specify a path for stdin [default: None]
# --stdout=<stdout>                 Specify a path for stdout [default: None]
# --stderr=<stderr>                 Specify a path for stdout [default: None]


def findCommand(name, commands):

    # Get the module corresponding to the command name
    module = getattr(commands, name)

    # Get the classes
    commandclass = getmembers(module, isclass)

    try:
        # Try running the first BaseCmd inherited class found
        command = [clss for cname, clss in commandclass
                   if issubclass(clss, BaseCmd)
                   and cname.lower() == name.lower()][0]
    except IndexError:
        raise AttributeError("module \n\% s\n do not contain a subclass of\
        BaseCmd with name % s(case insensitive)" % (module, name))

    dbg.debug("command", command)
    dbg.debug("command.run", command.run)

    return command


def main():
    """Main CLI entrypoint."""
    import taskgrader.commands

    # If args given in shell doesn't check with usage then
    # the programs stop
    options = docopt(clr.colorize(__doc__),
                     version=VERSION,
                     options_first=True)
    dbg.info("Launching...")
    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(taskgrader.commands, k) and v:
            command = findCommand(k, taskgrader.commands)
            command = command(options)
            command.run()
    dbg.info("Execution ended!")
