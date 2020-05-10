import tkinter
from tkinter_math.calculation import *

def sub_window_13():
    def calc_13():
        try:
            formula=txt_13_1.get()

            anser=Expand.Expand(formula)
        except:
            anser="Error"
        txt_13_2.delete(0,tkinter.END)
        txt_13_2.insert(0,anser)

    root_13=tkinter.Toplevel()
    root_13.title(u"展開")
    root_13.geometry("1000x300")
    root_13.resizable(False, False)

    btn_13_1=tkinter.Button(root_13,text="計算",command=calc_13,width=40,height=3)
    btn_13_1.place(x=330,y=110)
    btn_13_2=tkinter.Button(root_13,text="展開を閉じる",command=root_13.destroy,width=40,height=2,bg="#ffa300")
    btn_13_2.place(x=330,y=240)

    txt_13_1=tkinter.Entry(root_13,width=40,font=("",30))
    txt_13_1.place(x=70,y=50)
    txt_13_2=tkinter.Entry(root_13,width=40,font=("",30))
    txt_13_2.place(x=70,y=180)

    lbl_13_1=tkinter.Label(root_13,text="展開したい式を入力してください",font=("",15))
    lbl_13_1.place(x=330,y=20)

    root_13.mainloop()
