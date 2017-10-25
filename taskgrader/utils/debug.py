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


def display(mess, lvl):

    if lvl >= VERBOSE_RESI:
        mess = clr.colorize(mess)
        print(mess)


def error(*mess):
    display("{red}{bold}Error !{ec} " + " ".join(map(str, mess)), 40)


def warninfo(*mess):
    display("{wrn}{bold}\tWarning !{ec} " + " ".join(map(str, mess)), 30)


def info(*mess):
    display("{green}{bold} Info : {ec}" + " ".join(map(str, mess)), 20)


def debug(*mess, origin=None, force=False):

    if origin is None:
        origin = getCallerName()
    if len(mess) == 2:
        mess = ["val " + str(mess[0]) + " = " + str(mess[1])]

    mess = list(map(str, mess))
    display(clr.colorize("Debug from {blue}{bold} %s {ec} => %s" % (
        origin, " ".join(mess))), 0)


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
