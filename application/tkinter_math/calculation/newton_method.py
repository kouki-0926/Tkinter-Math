from tkinter_math.calculation.common.NEWTON_METHOD import NEWTON_METHOD

def newton_method(number):
    try:
        if float(number)>0:
            anser="="+str(NEWTON_METHOD(number))
            Anser=[number,anser]
        else:
            Anser=["Error",""]
            flash("エラー：正の数を入力してください")
    except:
        Anser=["Error",""]
    return Anser
