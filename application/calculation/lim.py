from sympy import *

x = Symbol('x')

def lim(formula,a):
    anser = limit(formula, x, a)

    return anser
