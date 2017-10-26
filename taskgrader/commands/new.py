from .base import BaseCmd
from ..utils import debug as dbg
from ..core import task as tsk
from ..utils import niceAsk as nA
import sys


class New(BaseCmd):

    def run(self):

        dbg.info("Creating a new Task..")
        task = tsk.Task()
        dbg.info(task.longDescription())

        file = nA.open_for_writing(".task")

        if file is None:
            dbg.error("Aborting process due to user choice")
            sys.exit(2)

        tsk.writeTaskFile(file, task)
        dbg.info("Created successfuly a '.task' file !")
