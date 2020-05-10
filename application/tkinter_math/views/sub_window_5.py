import tkinter
from tkinter_math.calculation import *

def sub_window_5():
    def calc_5():
        try:
            formula=txt_5_1.get()
            dimension=int(txt_5_3.get())
            center=float(txt_5_4.get())

            anser=taylor.taylor(formula,dimension,center)
        except:
            anser="Error"
        txt_5_2.delete("1.0",tkinter.END)
        txt_5_2.insert("1.0",anser)

    root_5=tkinter.Toplevel()
    root_5.title(u"テーラー展開")
    root_5.geometry("1500x700")
    root_5.resizable(False, False)

    btn_1=tkinter.Button(root_5,text="計算",command=calc_5,font=("",30),width=20)
    btn_1.place(x=150,y=110)
    btn_2=tkinter.Button(root_5,text="テーラー展開を閉じる",command=root_5.destroy,font=("",15),width=40,bg="#ffa300")
    btn_2.place(x=150,y=650)

    txt_5_1=tkinter.Entry(root_5,width=72,font=("",30))
    txt_5_1.place(x=30,y=40)
    txt_5_2=tkinter.Text(root_5,width=72,height=11,font=("",30))
    txt_5_2.place(x=30,y=200)
    txt_5_3=tkinter.Entry(root_5,width=3,font=("",25))
    txt_5_3.place(x=900,y=120)
    txt_5_4=tkinter.Entry(root_5,width=3,font=("",25))
    txt_5_4.place(x=1020,y=120)
    txt_5_5=tkinter.Entry(root_5,width=3,font=("",25))
    txt_5_5.place(x=1350,y=120)
    txt_5_6=tkinter.Entry(root_5,width=3,font=("",25))
    txt_5_6.place(x=1420,y=120)

    lbl_5_1=tkinter.Label(root_5,text="次数",font=("",25))
    lbl_5_1.place(x=800,y=120)
    lbl_5_2=tkinter.Label(root_5,text="x=",font=("",25))
    lbl_5_2.place(x=980,y=120)
    lbl_5_3=tkinter.Label(root_5,text="周り",font=("",25))
    lbl_5_3.place(x=1070,y=120)
    lbl_5_4=tkinter.Label(root_5,text="関数を入力してください",font=("",20))
    lbl_5_4.place(x=0,y=0)

    txt_5_3.insert(0,10)
    txt_5_4.insert(0,0)
    txt_5_5.insert(0,15)
    txt_5_6.insert(0,1)

    root_5.mainloop()
