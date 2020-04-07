from sympy import *

def calculation(A,B,Ar,Ac,Br,Bc,type,k,l):
    try:
        if type==0:
            anser=A
            type="A"
            anser_r=Ar
            anser_c=Ac

        elif type==1:
            anser=B
            type="B"
            anser_r=Br
            anser_c=Bc

        elif type==2:
            anser=k*A+l*B
            type=str(k)+"A+"+str(l)+"B"
            anser_r=Ar
            anser_c=Ac

        elif type==3:
            anser=A*B
            type="AB"
            anser_r=Ar
            anser_c=Bc

        elif type==4:
            anser=B*A
            type="BA"
            anser_r=Br
            anser_c=Ac

    except:
        anser=None
        type="Error"
        g=None
        h=None
    Anser=[anser,type,anser_r,anser_c]

    return Anser
