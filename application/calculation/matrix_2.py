from sympy import *

def calculation(A,B,Ar,Ac,Br,Bc,e,k,l):
    try:
        Anser=[]
        if e==0:
            anser=A
            type="A"
            anser_r=Ar
            anser_c=Ac

        elif e==1:
            anser=B
            type="B"
            anser_r=Br
            anser_c=Bc

        elif e==2:
            anser=k*A+l*B
            type=str(k)+"A+"+str(l)+"B"
            anser_r=Ar
            anser_c=Ac

        elif e==3:
            anser=A*B
            type="AB"
            anser_r=Ar
            anser_c=Bc

        elif e==4:
            anser=B*A
            type="BA"
            anser_r=Br
            anser_c=Ac

    except:
        anser=None
        type="Error"
        g=None
        h=None

    Anser.append(anser)
    Anser.append(type)
    Anser.append(anser_r)
    Anser.append(anser_c)

    return Anser
