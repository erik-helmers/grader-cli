from ..utils import debug as dbg
from ..utils import coloration as clr
from ..utils.getch import getch
import os
import sys

YES = {"yes", "ye", "y", "yeah", "yay"}
NO = {"no", "n", "nooo", "noo"}

YES_NO_ANSWERS = {
    1: "\t\tPlease answer {wrn}{bold} YES {ec} or {wrn}{bold} NO {ec} :",
    5: "Fuck off."
}


def yes_no_question(question, default="yes"):
    count = 0
    done = False

    if default in YES:
        message = question + " [YES/no] : "
    elif default in NO:
        message = question + " [yes/NO] : "
    else:
        message = question + " [yes/no] : "

    while not done:
        print(clr.colorize(message), end="")
        sys.stdout.flush()
        answer = getch()
        if answer in ["", "\n", " ", "\r"]:
            answer = default
        if answer in YES:
            return True
        elif answer in NO:
            return False
        count += 1
        message = YES_NO_ANSWERS.get(count, message)


def open_for_writing(filename, mode="w+", default=""):

    if os.path.exists(filename):
        answer = yes_no_question(
            "{red}{bold}\n\t\t\tWARNING  ! {ec} \n\
     File '%s' exists, override and continue ? " % (filename), "")
        if answer:
            dbg.info("OK... Let's continue and override.")

        else:
            raise FileExistsError()

    return open(filename, mode)


def open_for_reading(filename, mode="r"):

    if not os.path.exists(filename):
        raise FileNotFoundError()
    return open(filename, mode)
