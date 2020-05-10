from tkinter_math.calculation.common.NEWTON_METHOD import NEWTON_METHOD

def newton_method(number):
    try:
        if float(number)>0:
            anser=str(NEWTON_METHOD(number))
        else:
            anser="Error"
    except:
        anser="Error"
    return anser
