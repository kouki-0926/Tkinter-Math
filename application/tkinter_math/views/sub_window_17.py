import tkinter
from tkinter_math.calculation import *

def sub_window_17():
    def calc_17():
        try:
            formula=int(txt_17_1.get())

            anser=newton_method.newton_method(formula)
        except:
            anser="Error"
        txt_17_2.delete(0,tkinter.END)
        txt_17_2.insert(0,anser)

    root_17=tkinter.Toplevel()
    root_17.title(u"ニュートン法")
    root_17.geometry("600x170")
    root_17.resizable(False, False)

    txt_17_1=tkinter.Entry(root_17,width=3,font=("",30))
    txt_17_1.place(x=90,y=20)
    txt_17_2=tkinter.Entry(root_17,width=18,font=("",30))
    txt_17_2.place(x=220,y=20)

    lbl_17_1=tkinter.Label(root_17,text="sqrt(",font=("",30))
    lbl_17_1.place(x=0,y=20)
    lbl_17_2=tkinter.Label(root_17,text=") = ",font=("",30))
    lbl_17_2.place(x=150,y=20)

    btn_17_1=tkinter.Button(root_17,width=35,height=2,text="計算",command=calc_17)
    btn_17_1.place(x=150,y=70)
    btn_17_2=tkinter.Button(root_17,width=35,height=1,text="ニュートン法を閉じる",command=root_17.destroy,bg="#ffa300")
    btn_17_2.place(x=150,y=120)

    root_17.mainloop()
