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
            A = diff(formula,x,x)
        elif type=="xy":
            A = diff(formula,x,y)
        elif type=="yx":
            A = diff(formula,y,x)
        elif type=="yy":
            A = diff(formula,y,y)

        A=str(A)
        anser=A.replace("**","A").replace("*","").replace("A","^")
    except:
        anser="Error"
    return anser
