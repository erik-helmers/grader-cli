from .base import BaseCmd
from ..core import task as tsk
from ..utils import debug as dbg


class Load(BaseCmd):

    def run(self):
        file = open(".task", "r")
        task = tsk.Task(**tsk.parseTaskFile(file))
        dbg.debug("task", task)
        return task
