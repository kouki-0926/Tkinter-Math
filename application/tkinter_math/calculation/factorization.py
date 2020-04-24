from sympy import *
from tkinter_math.calculation.common.STR import STR

def factorization(formula):
    try:
        A=factor(formula)
        anser=STR(formula)+" = "+STR(A)
    except:
        anser="Error"
    return anser
