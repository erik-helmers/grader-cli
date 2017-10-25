""" This defines the task struct, the parser, etc..."""

import os
from ..utils import debug as dbg
from .. import __version__ as VERSION
from ..utils.coloration import colorize
from json import dumps
from inspect import getmembers


def path(filepath):

    if filepath[0] != "/":
        filepath = os.getcwd() + "/" + filepath
    if os.path.isfile(filepath):
        path = filepath
    else:
        raise FileNotFoundError("File not found at " + filepath)
    return path


def paths(filepaths):
    paths = []
    if isinstance(filepaths, str):
        filepaths.replace(" ", "")
        filepaths.split(",")
    for filepath in filepaths:
        if filepath != "":
            paths.append(path(filepath))
    return paths


class ParsingException(Exception):

    def __init__(self, message, errors=None):

        dbg.error(message)

        super(ParsingException, self).__init__()


TASK_STRUCT = {
    "name": str,
    "checker": path,
    "tests_in": paths,
    "tests_out": paths,
    "solutions": paths,
    "taskversion": str,
}


def parseTaskFile(file):

    output = {}

    for line in file:

        line = line.strip()

        if line[0] == "#":
            continue

        parts = line.split("=")

        if len(parts) != 2:
            raise ParsingException(
                "Malformed line: %s, needs exactly one line" % (line))

        if parts[0] not in TASK_STRUCT and parts[0] not in output:
            raise ParsingException(
                "Malformed line: %s, %s not in TASK_STRUCT keys" % (
                    line, parts[0]))

        valuetype = TASK_STRUCT[parts[0]]
        value = valuetype(parts[1])
        output[parts[0]] = value
    return output


def writeTaskFile(file, task):

    attributes = [(k, v) for k, v in getmembers(task) if k in TASK_STRUCT]
    for k, v in attributes:
        if isinstance(v, list):
            v = ",".join(str(v))
        elif v is None:
            continue
        file.write("%s = %s\n" % (k, v))


class Task:

    def __init__(self, **kwargs):

        self.name = kwargs.get("name", "untilted")
        self.version = kwargs.get("taskversion", VERSION)

        self.checker = kwargs.get("checker", None)
        self.test_in = kwargs.get("test_in", [])
        self.test_out = kwargs.get("test_out", [])
        self.solutions = kwargs.get("solutions", [])

        if len(self.test_in) != len(self.test_out):
            dbg.warninfo("test_in and test_out should be same length. \
\t\tNo tests will be avaible")
            self.test_in, self.test_out = [], []

    def longDescription(self):
        attributes = [(k, v) for k, v in getmembers(self)
                      if k in TASK_STRUCT and k != "name"]

        return colorize("About {blue}{bold}%s {ec}:\n" % (self.name) +
                        "\n".join(["\t - %s = %s" % (str(k), str(v))
                                   for (k, v) in attributes]))
