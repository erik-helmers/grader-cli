"""Exec command"""

from .base import BaseCmd
from ..core import runC


class Exec(BaseCmd):

    def run(self):
        stds = [self.options["<stdin>"],
                self.options["<stdout>"],
                self.options["<stderr>"]]

        stds = [(None if x == "None" else x) for x in stds]

        runC.run(self.options["<filename>"], *stds)
