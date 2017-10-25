"""The hello command."""


from json import dumps
from .base import BaseCmd
from ..core import coloration as clr


class Hello(BaseCmd):
    """Say hello, world!"""

    def run(self):
        print(clr.colorize("{bold}{blue} Hello World !\n"))
        print('You supplied the following options:',
              dumps(self.options, indent=4, sort_keys=True))
