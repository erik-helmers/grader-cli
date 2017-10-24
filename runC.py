""" Lance le programme selon son type"""

import sys
import subprocess as sb
import shlex
import os


OCAML_CMD = {"compile": "ocamlc -o {base}.out {file_name}",
             "exec": "{cwd}/{base}.out"}
PYTHON_CMD = {"exec": "python {file_name}"}
LAUNCHABLE = {"exec": "{cwd}/{file_name}"}

DEBUG = False
printback = print


def print_debug(*args, **kwargs):
    if DEBUG:
        printback(*args, **kwargs)


print = print_debug

EXTENSIONS = {".py": PYTHON_CMD, ".ml": OCAML_CMD, "": LAUNCHABLE}


def try_open(path, mode):
    if path[0] != "/":
        path = os.getcwd() + "/" + path
    try:
        return open(path, mode)
    except Exception as e:
        print(e)
        return None


def try_open_multi(paths, modes):
    otpt = []
    for path, mode in zip(paths, modes):
        otpt.append(try_open(path, mode))
    return otpt


def close_all(l):
    for f in l:
        try:
            f.close()
        except:
            pass


def get_extensions(filename):
    return os.path.splitext(filename)


def run(filename, stdin=None, stdout=None, stderr=None):
    base, extension = get_extensions(filename)

    if extension not in EXTENSIONS:
        raise ValueError(
            "Le fichier de type %s n'est pas supporté" % (extension))

    act = EXTENSIONS[extension]

    if act.get("compile"):
        p1 = sb.Popen(shlex.split(
            act["compile"].format(file_name=filename,
                                  base=base, cwd=os.getcwd())))

    p1 = sb.Popen(shlex.split(act["exec"].format(file_name=filename,
                                                 base=base, cwd=os.getcwd())),
                  stdin=stdin, stdout=stdout, stderr=stderr)
    return p1.communicate()


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
