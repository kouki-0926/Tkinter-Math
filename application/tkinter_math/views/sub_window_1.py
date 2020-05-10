import tkinter
from tkinter_math.calculation import *

def sub_window_1():
    def calc_1():
        try:
            formula=txt_1_1.get()
            type=txt_1_3.get()
            anser=derivative.derivative(formula,type)
        except:
            anser="Error"
        txt_1_2.delete(0,tkinter.END)
        txt_1_2.insert(0,anser)

    root_1=tkinter.Toplevel()
    root_1.title(u"微分")
    root_1.geometry("1500x300")
    root_1.resizable(False, False)

    btn_1_1=tkinter.Button(root_1,text="計算",width=20,command=calc_1,font=("",20))
    btn_1_1.place(x=500,y=130)
    btn_1_2=tkinter.Button(root_1,text="微分を閉じる",width=40,command=root_1.destroy,font=("",10),bg="#ffa300")
    btn_1_2.place(x=500,y=260)

    txt_1_1=tkinter.Entry(root_1,width=73,font=("",30))
    txt_1_1.place(x=20,y=50)
    txt_1_2=tkinter.Entry(root_1,width=73,font=("",30))
    txt_1_2.place(x=20,y=200)
    txt_1_3=tkinter.Entry(root_1,width=2,font=("",30))
    txt_1_3.place(x=1000,y=130)

    lbl_1_1=tkinter.Label(root_1,text="関数を入力してください",font=("",20))
    lbl_1_1.place(x=20,y=15)
    lbl_1_2=tkinter.Label(root_1,text="導関数",font=("",20))
    lbl_1_2.place(x=20,y=165)

    txt_1_3.insert(0,"x")

    root_1.mainloop()
