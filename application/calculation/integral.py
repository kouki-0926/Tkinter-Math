from sympy import *
from calculation.common.STR import STR

x = Symbol('x')

def integral(formula,upper_end,lower_end,type):
    try:
        g=integrate(formula)
        A=g.subs(x,upper_end)-g.subs(x,lower_end)

        if type==0:
            anser=str(A)
        elif type==1:
            anser=str(A.evalf())
        elif type==2:
            anser=STR(g)+"+C"
    except:
        anser="Error"
    return anser
