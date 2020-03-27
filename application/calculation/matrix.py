from sympy import *

def calculation(A,a,b,c):
    try:
        anser=[]
        if c==0:
            A=A
            D="A"
            d=0

        elif c==1:
            A=A**2
            D="A^2"
            d=0

        elif c==2:
            A=A.transpose()
            D="A^t"
            b=a
            d=0

        elif c==3:
            A=A.inv()
            D="A^-1"
            d=0

        elif c==4:
            A=A.adjugate()
            D="A~"
            d=0

        elif c==5:
            A=A.det()
            D="det(A)"
            d=1

        elif c==6:
            A=A.rank()
            D="rank(A)"
            d=1

        elif c==7:
            A=A.trace()
            D="tr(A)"
            d=1

        elif c==8:
            A=A.eigenvals()
            A=list(A)
            D="λ"
            d=1

        elif c==9:
            A=A.diagonalize()
            A=list(A)
            A=A[0]
            D="P"
            d=0

        elif c==10:
            A=A.diagonalize()
            A=list(A)
            A=A[1]
            D="P^-1AP"
            d=0
    except:
        A="Error"
        D="Error"
        d=1

    anser.append(A)
    anser.append(D)
    anser.append(d)
    anser.append(b)

    return anser
