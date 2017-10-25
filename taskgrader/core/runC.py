""" Lance le programme selon son type"""

import sys
import subprocess as sb
import shlex
import os
from ..utils import debug as dbg

OCAML_CMD = {"compile": "ocamlc -o {base}.out {file_name}",
             "exec": "{cwd}/{base}.out"}
PYTHON_CMD = {"exec": "python {file_name}"}
LAUNCHABLE = {"exec": "{cwd}/{file_name}"}


def get_extensions(filename):
    return os.path.splitext(filename)


EXTENSIONS = {".py": PYTHON_CMD, ".ml": OCAML_CMD, "": LAUNCHABLE}

STDEXTENSION = [(0, "r", ".in"), (1, "a", ".out"), (2, "a", "")]


def try_open(path, mode):

    if path[0] != "/":
        path = os.getcwd() + "/" + path
    try:
        return open(path, mode)
    except FileNotFoundError as e:
        dbg.warninfo('File %s not found ! Using default instead...' % (path))
        return None


def try_open_multi(paths, modes):
    otpt = []
    for path, mode in zip(paths, modes):
        otpt.append(try_open(path, mode))
    return otpt


def checkExtension(path, expect):
    extension = get_extensions(path)[1]
    if extension != expect:
        dbg.warninfo("Unexpected extension file '%s' expected '%s'" % (
                     extension, expect))


def treatStds(stdin, stdout, stderr):

    stds = [stdin, stdout, stderr]

    for (i, mode, expectExtens), std in zip(STDEXTENSION, stds):

        if isinstance(std, str):
            stds[i] = try_open(std, mode)
            if stds[i]:
                checkExtension(std, expectExtens)
        elif std is None:
            pass
        else:
            dbg.warninfo("Unexpected value of type", type(std))
    return tuple(stds)


def close_all(l):
    for f in l:
        try:
            f.close()
        except:
            pass


def run(filename, stdin=None, stdout=None, stderr=None):

    base, extension = get_extensions(filename)

    dbg.debug("filename", filename)
    dbg.debug("stdin", repr(stdin))
    dbg.debug("stdout", repr(stdout))
    dbg.debug("stderr", repr(stderr))

    stdin, stdout, stderr = treatStds(stdin, stdout, stderr)

    if extension not in EXTENSIONS:
        raise ValueError(
            "Le fichier de type %s n'est pas supporté" % (extension))

    act = EXTENSIONS[extension]

    if act.get("compile"):
        p1 = sb.Popen(shlex.split(
            act["compile"].format(file_name=filename,
                                  base=base, cwd=os.getcwd())))
        p1.wait()

    p2 = sb.Popen(shlex.split(act["exec"].format(file_name=filename,
                                                 base=base, cwd=os.getcwd())),
                  stdin=stdin, stdout=stdout, stderr=stderr)
    p2.wait()

    return p2.communicate()


if __name__ == "__main__":

    if 2 <= len(sys.argv):

        if len(sys.argv) >= 3 and sys.argv[2] == '-d':
            DEBUG = True
            del sys.argv[2]

        stdentrys = try_open_multi(sys.argv[2:], ["r", "a", "a"])

        print(stdentrys)

        result = run(sys.argv[1], *stdentrys)
        print("got output:", result[0])
        print("errs:", result[1])

        close_all(stdentrys)

    else:
        print("No enough arguments")
