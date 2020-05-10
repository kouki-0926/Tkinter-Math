import tkinter
from tkinter_math.calculation import *

def sub_window_14():
    def calc_14():
        try:
            formula=txt_14_1.get()

            anser=prime_factorization.prime_factorization(formula)
        except:
            anser="Error"
        txt_14_2.delete(0,tkinter.END)
        txt_14_2.insert(0,anser)

    root_14=tkinter.Toplevel()
    root_14.title(u"素因数分解")
    root_14.geometry("1000x300")
    root_14.resizable(False, False)

    btn_14_1=tkinter.Button(root_14,text="計算",command=calc_14,width=40,height=3)
    btn_14_1.place(x=330,y=110)
    btn_14_2=tkinter.Button(root_14,text="素因数分解を閉じる",command=root_14.destroy,width=40,height=2,bg="#ffa300")
    btn_14_2.place(x=330,y=240)

    txt_14_1=tkinter.Entry(root_14,width=40,font=("",30))
    txt_14_1.place(x=70,y=50)
    txt_14_2=tkinter.Entry(root_14,width=40,font=("",30))
    txt_14_2.place(x=70,y=180)

    lbl_14_1=tkinter.Label(root_14,text="整数を入力してください",font=("",15))
    lbl_14_1.place(x=330,y=20)

    root_14.mainloop()
