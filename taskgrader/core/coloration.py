class Color:

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
        "udrln": UNDERLINE
    }

    shortcuts_none = {x: "" for x in shortcuts.keys()}

    @staticmethod
    def colorize(s):
        return s.format(
            **Color.shortcuts
        )

    @staticmethod
    def no_color(s):
        return s.format(
            **Color.shortcuts_none
        )
