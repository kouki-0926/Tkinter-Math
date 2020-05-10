import tkinter
from tkinter_math.calculation import *

def sub_window_9():
    def calc_9():
        try:
            formula=txt_9_1.get()
            a=txt_9_3.get()

            anser=lim.lim(formula,a)
        except:
            anser="Error"
        txt_9_2.delete(0,tkinter.END)
        txt_9_2.insert(0,anser)

    root_9=tkinter.Toplevel()
    root_9.title(u"極限")
    root_9.geometry("960x200")
    root_9.resizable(False, False)

    btn_9_1=tkinter.Button(root_9,text="計算",command=calc_9,width=40,height=2)
    btn_9_1.place(x=330,y=110)
    btn_9_2=tkinter.Button(root_9,text="極限を閉じる",command=root_9.destroy,width=40,height=1,bg="#ffa300")
    btn_9_2.place(x=330,y=155)

    lbl_9_1=tkinter.Label(root_9,text="lim",font=("",40))
    lbl_9_1.place(x=20,y=20)
    lbl_9_2=tkinter.Label(root_9,text="X →",font=("",15))
    lbl_9_2.place(x=20,y=80)
    lbl_9_3=tkinter.Label(root_9,text="=",font=("",50))
    lbl_9_3.place(x=650,y=30)

    txt_9_1=tkinter.Entry(root_9,width=16,font=("",50))
    txt_9_1.place(x=100,y=30)
    txt_9_2=tkinter.Entry(root_9,width=7,font=("",50))
    txt_9_2.place(x=700,y=30)
    txt_9_3=tkinter.Entry(root_9,width=2,font=("",15))
    txt_9_3.place(x=65,y=80)

    txt_9_3.insert(0,0)

    root_9.mainloop()
