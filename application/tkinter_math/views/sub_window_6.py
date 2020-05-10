import tkinter
from tkinter_math.calculation import *

def sub_window_6():
    def calc_6():
        try:
            formula=int(txt_6_1.get())

            anser=Factorial.Factorial(formula)
        except:
            anser="Error"
        txt_6_2.delete(0,tkinter.END)
        txt_6_2.insert(0,anser)

    root_6=tkinter.Toplevel()
    root_6.title(u"階乗")
    root_6.geometry("440x160")
    root_6.resizable(False, False)

    txt_6_1=tkinter.Entry(root_6,width=3,font=("",30))
    txt_6_1.place(x=20,y=20)
    txt_6_2=tkinter.Entry(root_6,width=13,font=("",30))
    txt_6_2.place(x=150,y=20)

    lbl_6_1=tkinter.Label(root_6,text="!  =",font=("",30))
    lbl_6_1.place(x=90,y=20)

    btn_6_1=tkinter.Button(root_6,width=35,height=2,text="計算",command=calc_6)
    btn_6_1.place(x=100,y=70)
    btn_6_2=tkinter.Button(root_6,width=35,height=1,text="階乗を閉じる",command=root_6.destroy,bg="#ffa300")
    btn_6_2.place(x=100,y=120)

    root_6.mainloop()
