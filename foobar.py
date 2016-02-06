
from math import log

def instr_index(n, x):

    s = (3 ** n - 1) / 2
    right = int((x + s) / 3 ** n)
    return right % 3

def no_of_steps(x):
    return int(log(x * 2, 3)) + 1

def answer(x):


    instr = []
    steps = no_of_steps(x)

    for n in xrange(steps):
        i = instr_index(n, x)
        instr.append(['-', 'R', 'L'][i])

    return instr

