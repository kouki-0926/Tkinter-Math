from sympy import *
from calculation.common.STR import STR

def factorization(formula):
    try:
        A=factor(formula)
        anser=STR(formula)+" = "+STR(A)
    except:
        anser="Error"
    return anser
