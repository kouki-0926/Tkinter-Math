import tkinter
from tkinter_math.calculation import *

def sub_window_15():
    def calc_15():
        try:
            number_x=txt_15_1.get()
            number_y=txt_15_2.get()
            anser=Euclidean_Algorithm.Euclidean_Algorithm(number_x,number_y)
        except:
            anser="Error"
        txt_15_3.delete(0,tkinter.END)
        txt_15_3.insert(0,anser)

    root_15=tkinter.Toplevel()
    root_15.title(u"ユークリッドの互除法")
    root_15.geometry("650x380")
    root_15.resizable(False, False)

    btn_15_1=tkinter.Button(root_15,text="計算",command=calc_15,width=40,height=3)
    btn_15_1.place(x=180,y=160)
    btn_15_2=tkinter.Button(root_15,text="ユークリッドの互除法を閉じる",command=root_15.destroy,width=40,height=2,bg="#ffa300")
    btn_15_2.place(x=180,y=300)

    txt_15_1=tkinter.Entry(root_15,width=30,font=("",30))
    txt_15_1.place(x=20,y=50)
    txt_15_2=tkinter.Entry(root_15,width=30,font=("",30))
    txt_15_2.place(x=20,y=100)
    txt_15_3=tkinter.Entry(root_15,width=30,font=("",30))
    txt_15_3.place(x=20,y=230)

    lbl_15_1=tkinter.Label(root_15,text="整数を入力してください",font=("",15))
    lbl_15_1.place(x=70,y=20)

    root_15.mainloop()
