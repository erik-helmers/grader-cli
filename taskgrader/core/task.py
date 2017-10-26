""" This defines the task struct, the parser, etc..."""

from json import dumps
import os
from ..utils import debug as dbg
from .. import __version__ as VERSION
from ..utils.coloration import colorize
from json import dumps
from inspect import getmembers


def path(filepath):

    path = filepath

    if path[0] != "/":
        path = os.getcwd() + "/" + path
    if not os.path.isfile(path):
        raise FileNotFoundError("File not found at " + path)

    return filepath


def paths(filepaths):
    paths = []

    if isinstance(filepaths, str):
        filepaths = filepaths.replace(" ", "")
        filepaths = filepaths.split(",")

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

        if line[0] == "#" or line == '':
            continue

        parts = list(map(str.strip, line.split("=")))

        if len(parts) == 1 and parts[0] in TASK_STRUCT:
            parts.append("")

        if len(parts) != 2:
            raise ParsingException(
                "Malformed line: %s, needs exactly one line" % (line))

        if parts[0] not in TASK_STRUCT or parts[0] in output:
            raise ParsingException(
                "Malformed line: '%s', '%s' not in TASK_STRUCT keys" % (
                    line, parts[0]))

        dbg.debug("parts", parts)

        valuetype = TASK_STRUCT[parts[0]]
        value = valuetype(parts[1])
        output[parts[0]] = value
    dbg.debug("output", dumps(output, indent=4), wcolor=False)
    return output


def writeTaskFile(file, task):

    attributes = [(k, v) for k, v in getmembers(task) if k in TASK_STRUCT]
    dbg.debug("attributes", dumps(attributes, indent=4), wcolor=False)
    for k, v in attributes:
        if isinstance(v, list):
            v = ",".join(v)
        elif v is None:
            continue
        file.write("%s = %s\n" % (k, v))
    file.flush()


class Task:

    def __init__(self, **kwargs):

        self.name = kwargs.get("name", "untilted")
        self.taskversion = kwargs.get("taskversion", VERSION)

        self.checker = kwargs.get("checker", None)
        self.tests_in = kwargs.get("tests_in", [])
        self.tests_out = kwargs.get("tests_out", [])
        self.solutions = kwargs.get("solutions", [])

        if len(self.tests_in) != len(self.tests_out):
            dbg.warninfo("test_in and test_out should be same length. \
\t\tNo tests will be avaible")
            self.test_in, self.test_out = [], []

    def longDescription(self):
        attributes = [(k, v) for k, v in getmembers(self)
                      if k in TASK_STRUCT and k != "name"]

        return ("About {bold} %s {ec}:\n") % (self.name) + "\n".join(
            ["\t - %s = %s" % (str(k), str(v))
             for (k, v) in attributes])

    def addTest(self, inpath, outpath):

        inname, inext = os.path.splitext(inpath)
        outname, outext = os.path.splitext(outpath)

        if inext != ".in":
            dbg.warninfo("Input file must have '.in' ext, got '%s'" %
                         (inext))
        if outext != ".out":
            dbg.warninfo("Output file must have '.out' ext, got '%s'" %
                         (outext))

        if outname != inname:
            dbg.warninfo(
                "It's recommended to have same file name for in and out file")

        self.tests_in.append(inpath)
        self.tests_out.append(outpath)
