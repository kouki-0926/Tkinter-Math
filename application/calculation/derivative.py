from sympy import *

x = Symbol('x')
y = Symbol('y')

def derivative(formula,type):
    try:
        if type=="x":
            A = diff(formula,x)
        elif type=="y":
            A = diff(formula,y)
        elif type=="xx":
            f = diff(formula,x)
            A = diff(f,x)
        elif type=="xy":
            f = diff(formula,x)
            A = diff(f,y)
        elif type=="yx":
            f = diff(formula,y)
            A = diff(f,x)
        elif type=="yy":
            f = diff(formula,y)
            A = diff(f,y)

        A=str(A)
        anser=A.replace("**","A").replace("*","").replace("A","^")
    except:
        anser="Error"
    return anser
