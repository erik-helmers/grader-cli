"""The base command."""


class BaseCmd(object):
    """A base command."""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def run(self):
        raise NotImplementedError('Cette methode doit être overridée')

    @classmethod
    def isCmd(clss):
        return clss.__name__ != "BaseCmd"
