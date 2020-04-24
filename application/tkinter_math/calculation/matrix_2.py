from sympy import *

def calculation(A,B,Ar,Ac,Br,Bc,type,k,l):
    try:
        if type=="A":
            anser=A
            anser_r=Ar
            anser_c=Ac

        elif type=="B":
            anser=B
            anser_r=Br
            anser_c=Bc

        elif type=="kA+lB":
            anser=k*A+l*B
            type=str(k)+"A+"+str(l)+"B"
            anser_r=Ar
            anser_c=Ac

        elif type=="AB":
            anser=A*B
            anser_r=Ar
            anser_c=Bc

        elif type=="BA":
            anser=B*A
            anser_r=Br
            anser_c=Ac
    except:
        anser="Error"
        type=""
        anser_r=""
        anser_c=""
    Anser=[anser,type,anser_r,anser_c]

    return Anser
