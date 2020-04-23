from sympy import *
from calculation.common.STR import STR

x = Symbol('x')

def taylor(formula,dimension,center):
    try:
        f=sympify(formula)
        center=float(center)

        A=f.subs(x,center)
        for number in range(1,int(dimension)+1,1):
            f=diff(f)
            D=f.subs(x,center)/factorial(number)
            A=D*(x-center)**number+A

        anser=STR(formula)+"≒"+STR(A)
        anser_2=str(formula)+"≒"+str(A)
        print("------------------------------------------------------------------------------------------------------------------------")
        print(anser+"\n\n"+anser_2+"\n")
    except:
        anser="Error"
        print("Error")
    return anser
