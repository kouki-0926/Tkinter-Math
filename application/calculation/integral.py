from sympy import *

x = Symbol('x')

def integral(formula,a,b,c):
    try:
        g=integrate(formula)
        A=g.subs(x,a)-g.subs(x,b)

        if  c==0:
            anser=A

        elif c==1:
            anser=A.evalf()

        elif c==2:
            g=str(g)
            anser=g.replace("**","A").replace("*","").replace("A","^")
    except:
        anser="Error"
    return anser
