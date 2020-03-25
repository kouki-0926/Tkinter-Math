from sympy import *

x = Symbol('x')
y = Symbol('y')

def derivative(formula,a):
    try:
        g = formula

        if a=="x":
            f = diff(g,x)
        elif a=="y":
            f = diff(g,y)
        elif a=="xx":
            f = diff(g,x)
            f = diff(f,x)
        elif a=="xy":
            f = diff(g,x)
            f = diff(f,y)
        elif a=="yx":
            f = diff(g,y)
            f = diff(f,x)
        elif a=="yy":
            f = diff(g,y)
            f = diff(f,y)

        f=str(f)
        anser=f.replace("**","A").replace("*","").replace("A","^")
    except:
        anser="Error"
    return anser
