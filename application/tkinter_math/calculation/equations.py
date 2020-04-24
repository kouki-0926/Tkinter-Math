from sympy import *
from tkinter_math.calculation.common.STR import STR

def equations(formula):
    try:
        A=list(solve(formula,dict=True))
        anser=[]
        for i in range(0,len(A),1):
            for B in A[i].items():
                anser.append(STR(B[0])+"="+STR(B[1]))
    except:
        anser=["Error"]
    return anser
