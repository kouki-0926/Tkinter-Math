from sympy import *

def calculation(A,Ar,Ac,type):
    try:
        if type=="A":
            anser=A
            anser_r=Ar
            anser_c=Ac
            insert_type="MATRIX"

        elif type=="A^n":
            A=A.diagonalize()
            A=list(A)
            P=A[0]
            D=A[1]
            for i in range(Ac):
                D[i,i]="("+str(D[i,i])+")^n"
            anser=P*D*P.inv()
            anser_r=Ar
            anser_c=Ac
            insert_type="MATRIX"

        elif type=="A^t":
            anser=A.transpose()
            anser_r=Ac
            anser_c=Ar
            insert_type="MATRIX"

        elif type=="A^-1":
            anser=A.inv()
            anser_r=Ar
            anser_c=Ac
            insert_type="MATRIX"

        elif type=="A~":
            anser=A.adjugate()
            anser_r=Ar
            anser_c=Ac
            insert_type="MATRIX"

        elif type=="det(A)":
            anser=A.det()
            anser_r=""
            anser_c=""
            insert_type="NUMBER"

        elif type=="rank(A)":
            anser=A.rank()
            anser_r=""
            anser_c=""
            insert_type="NUMBER"

        elif type=="tr(A)":
            anser=A.trace()
            anser_r=""
            anser_c=""
            insert_type="NUMBER"

        elif type=="λ":
            A=A.eigenvals()
            anser=list(A)
            anser_r=""
            anser_c=""
            insert_type="NUMBER"

        elif type=="P":
            A=A.diagonalize()
            A=list(A)
            anser=A[0]
            anser_r=Ar
            anser_c=Ac
            insert_type="MATRIX"

        elif type=="P^-1AP":
            A=A.diagonalize()
            A=list(A)
            anser=A[1]
            anser_r=Ar
            anser_c=Ac
            insert_type="MATRIX"
    except:
        anser="Error"
        anser_r=""
        anser_c=""
        type="Error"
        insert_type="NUMBER"

    Anser=[anser,anser_r,anser_c,type,insert_type]

    return Anser
