from .base import BaseCmd
from ..core import task as tsk
from ..utils import debug as dbg
from ..utils import coloration as clr
from ..utils import niceAsk
from .load import Load

import os


class Add(BaseCmd):

    def run(self):

        task = Load(None).run()

        infilename = self.options["<filename>"]
        outfilename = self.options["<outfilename>"]

        if outfilename is None:
            outfilename = os.path.splitext(infilename)[0] + ".out"

        task.addTest(infilename, outfilename)
        tsk.writeTaskFile(niceAsk.open_for_writing(".task"), task)
