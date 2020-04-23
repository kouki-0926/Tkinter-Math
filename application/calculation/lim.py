from sympy import *

x = Symbol('x')

def lim(formula,a):
    try:
        a=float(a)
        anser = limit(formula, x, a)
    except:
        anser="Error"
    return anser
