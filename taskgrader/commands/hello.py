"""The hello command."""


from json import dumps
from . import base
from .base import Base


class Hello(Base):
    """Say hello, world!"""

    def run(self):
        print(base.bcolors.WARNING + 'Hello, world!' + base.bcolors.ENDC)
        print('You supplied the following options:',
              dumps(self.options, indent=4, sort_keys=True))
