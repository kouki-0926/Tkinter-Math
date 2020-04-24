from sympy import *
from tkinter_math.calculation.common.STR import STR

def Expand(formula):
    try:
        A=expand(formula)
        anser=STR(formula)+" = "+STR(A)
    except:
        anser="Error"
    return anser
