from sympy import *

def calculation(A,B,a,b,c,d,e,k,l):
    try:
        Anser=[]
        if e==0:
            anser=A
            type="A"
            g=a
            h=b

        elif e==1:
            anser=B
            type="B"
            g=c
            h=d

        elif e==2:
            anser=k*A+l*B
            type=str(k)+"A+"+str(l)+"B"
            g=a
            h=b

        elif e==3:
            anser=A*B
            type="AB"
            g=a
            h=d

        elif e==4:
            anser=B*A
            type="BA"
            g=c
            h=b
    except:
        anser=None
        type="Error"
        g=None
        h=None

    Anser.append(anser)
    Anser.append(type)
    Anser.append(g)
    Anser.append(h)

    return Anser
