"""Task Grader:
  évalue une solution à un problème,
  pour cela, prend un fichier .in,
  execute le programme, puis compare la
  sortie avec un fichier .out"""

import subprocess as sb
from shlex import split
import sys
import runC


def grad(fname, inf, outf):

    pass


solF, inF, outF = sys.argv[1:]

p1 = sb.Popen(split("cat " + inF), stdout=sb.PIPE)
output, error = getOutputFromSol(solF, p1.stdout)
print("Got : ", repr(output))

score = 0
maxScore = 0
with open(outF, "r") as f:
    print("Expected :")
    for x in f:
        print(x)
    f.close()


#     result = p2.communicate()[0]    #

# print("Got :")
# for x in result:
#     print(x)
# for expected, got in zip(open(outF, "r"), result):
#     maxScore += 1
#     if expected == got:
#         score += 1

# print("Solution got %d on %d" % (score, maxScore))

if __name__ = "__main__":
