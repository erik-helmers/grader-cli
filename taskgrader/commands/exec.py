"""Exec command"""

from .base import BaseCmd


class Exec(BaseCmd):

    def run(self):
        print("got: " + str(self.args))
        print("got: " + str(self.kwargs))
        print("got: " + str(self.options))
