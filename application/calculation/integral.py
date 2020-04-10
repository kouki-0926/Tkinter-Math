from sympy import *

x = Symbol('x')

def integral(formula,upper_end,lower_end,type):
    try:
        g=integrate(formula)
        A=g.subs(x,upper_end)-g.subs(x,lower_end)

        if type==0:#定積分
            anser=A
        elif type==1:#定積分(浮動小数点数)
            anser=A.evalf()
        elif type==2:#不定積分
            g=str(g)
            anser=g.replace("**","A").replace("*","").replace("A","^")
    except:
        anser="Error"
    return anser
