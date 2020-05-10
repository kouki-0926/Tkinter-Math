import tkinter
from tkinter_math.calculation import *

def sub_window_2():
    def calc_2():
        try:
            formula=txt_2_1.get()
            upper_end=txt_2_2.get()
            lower_end=txt_2_3.get()
            type=int(txt_2_5.get())

            anser=integral.integral(formula,upper_end,lower_end,type)
        except:
            anser="Error"
        txt_2_4.delete(0,tkinter.END)
        txt_2_4.insert(0,anser)

    root_2=tkinter.Toplevel()
    root_2.title(u"積分")
    root_2.geometry("1500x280")
    root_2.resizable(False, False)

    btn_2_1=tkinter.Button(root_2,text="計算",width=20,command=calc_2,font=("",20))
    btn_2_1.place(x=580,y=200)
    btn_2_2=tkinter.Button(root_2,text="積分を閉じる",width=40,command=root_2.destroy,font=("",10),bg="#ffa300")
    btn_2_2.place(x=580,y=250)

    txt_2_1=tkinter.Entry(root_2,width=20,font=("",40))
    txt_2_1.place(x=80,y=90)
    txt_2_2=tkinter.Entry(root_2,width=10)
    txt_2_2.place(x=30,y=50)
    txt_2_3=tkinter.Entry(root_2,width=10)
    txt_2_3.place(x=30,y=170)
    txt_2_4=tkinter.Entry(root_2,width=25,font=("",40))
    txt_2_4.place(x=800,y=90)
    txt_2_5=tkinter.Entry(root_2,width=1,font=("",30))
    txt_2_5.place(x=1400,y=10)

    lbl_2_1=tkinter.Label(root_2,text="∫",font=("",70))
    lbl_2_1.place(x=-20,y=70)
    lbl_2_2=tkinter.Label(root_2,text="dx =",font=("",60))
    lbl_2_2.place(x=620,y=70)
    lbl_2_3=tkinter.Label(root_2,text="数値を出力するときは１を入力")
    lbl_2_3.place(x=1220,y=10)
    lbl_2_4=tkinter.Label(root_2,text="不定積分を出力するときは2を入力")
    lbl_2_4.place(x=1220,y=30)

    txt_2_5.insert(0,0)

    root_2.mainloop()
