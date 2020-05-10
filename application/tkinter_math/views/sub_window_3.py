import tkinter
from tkinter_math.calculation import *

def sub_window_3():
    def calc_3():
        try:
            formula=txt_3_1.get()

            anser=factorization.factorization(formula)
        except:
            anser="Error"
        txt_3_2.delete(0,tkinter.END)
        txt_3_2.insert(0,anser)

    root_3=tkinter.Toplevel()
    root_3.title(u"因数分解")
    root_3.geometry("1000x300")
    root_3.resizable(False, False)

    btn_3_1=tkinter.Button(root_3,text="計算",command=calc_3,width=40,height=3)
    btn_3_1.place(x=330,y=110)
    btn_3_2=tkinter.Button(root_3,text="因数分解を閉じる",command=root_3.destroy,width=40,height=2,bg="#ffa300")
    btn_3_2.place(x=330,y=240)

    txt_3_1=tkinter.Entry(root_3,width=40,font=("",30))
    txt_3_1.place(x=70,y=50)
    txt_3_2=tkinter.Entry(root_3,width=40,font=("",30))
    txt_3_2.place(x=70,y=180)

    lbl_3_1=tkinter.Label(root_3,text="因数分解したい式を入力してください",font=("",15))
    lbl_3_1.place(x=330,y=20)

    root_3.mainloop()
