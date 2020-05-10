from tkinter_math.calculation.common.NEWTON_METHOD import NEWTON_METHOD

def Sieve_of_Eratosthenes(N):
    try:
        N=int(N)
        if N>=2:
            List=list(range(2,N+1))
            prime_List=[]

            MIN=0
            while MIN<NEWTON_METHOD(N):
                MIN=min(List)
                prime_List.append(MIN)
                List=[i for i in List if i % MIN != 0]
            prime_List=prime_List+List
            Anser=prime_List
        else:
            Anser="Error"
    except:
        Anser="Error"
    return Anser
