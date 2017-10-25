from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION

from .core.coloration import Color

helpmess = """
\n
{wrn}Task grader{ec}

This little utils let you test your solutions
by creating tests.

Usage:
  taskgrader hello
  taskgrader exec <filename>
  taskgrader -h | --help
  taskgrader --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  taskgrader hello

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/erik-helmers/grader-cli
"""

__doc__ = "hello fuck you"


def main():
    """Main CLI entrypoint."""
    import taskgrader.commands

    # If args given in shell doesn't check with usage then
    # the programs stop
    options = docopt(Color.no_color(helpmess), version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(taskgrader.commands, k) and v:
            module = getattr(taskgrader.commands, k)
            taskgrader.commands = getmembers(
                module, isclass)  # Get all commands
            command = [command[1]
                       for command in taskgrader.commands
                       if command[0] != 'Base'][0]
            command = command(options)
            command.run()
