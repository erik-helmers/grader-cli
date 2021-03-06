""" A simple colorization tool"""


HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

shortcuts = {
    "hd": HEADER,
    "blue": OKBLUE,
    "green": OKGREEN,
    "wrn": WARNING,
    "fail": FAIL,
    "ec": ENDC,
    "bold": BOLD,
    "udrln": UNDERLINE,
    "red": FAIL
}

shortcuts_none = {x: "" for x in shortcuts.keys()}


def colorize(s):
    return (s + "{ec}").format(
        **shortcuts
    )


def no_color(s):
    return s.format(
        **shortcuts_none

    )
