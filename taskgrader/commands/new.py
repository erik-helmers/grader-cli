from .base import BaseCmd
from ..utils import debug as dbg
from ..core import task as tsk


class New(BaseCmd):

    def run(self):
        dbg.info("Creating a new Task..")
        task = tsk.Task()
        dbg.info(task.longDescription())
