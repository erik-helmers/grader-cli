"""Exec command"""

from . import base
from .base import Base


class Exec(Base):

    def run(self):
        print(base.bcolors.WARNING +
              "Not yet implented" +
              base.bcolors.ENDC)
        print("got: " + str(self.args))
        print("got: " + str(self.kwargs))
        print("got: " + str(self.options))
