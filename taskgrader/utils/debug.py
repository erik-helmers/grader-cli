""" A debugger helper"""

import inspect
from . import coloration as clr

VERBOSE_RESI = 0
specials = {}


def WRITE_TO_NOTHING(*args, **kwargs):
    return


def getCallerName():
    "Return the name of the calling method"

    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 3)
    return calframe[2][3]


def debug(*mess, origin=None, force=False):

    if origin is None:
        origin = getCallerName()
    if len(mess) == 2:
        mess = ["val " + str(mess[0]) + " = " + str(mess[1])]

    mess = list(map(clr.colorize, mess))
    mess = list(map(str, mess))
    print(clr.colorize("{red}{bold} From: %s {ec} => %s" % (
        origin, " ".join(mess))))


def DebugForceTo(func, force):
    " if force then always debug else always mute "

    def wrapper(*args, **kwargs):

        global debug
        backup = debug

        debug = WRITE_TO_NOTHING if force else (
            lambda *x: backup(*x, getCallerName(), True))

        result = func(*args, **kwargs)

        debug = backup

        return result

    return wrapper
