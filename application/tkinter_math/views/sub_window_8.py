import tkinter
from tkinter_math.calculation import *

def sub_window_8():
    def calc_8():
        try:
            height=txt_8_1.get()
            weight=txt_8_2.get()
            anser=BMI.BMI(height,weight)
        except:
            anser=["Error","Error"]
        txt_8_3.delete(0,tkinter.END)
        txt_8_4.delete(0,tkinter.END)
        txt_8_3.insert(0,anser[0])
        txt_8_4.insert(0,anser[1])

    root_8=tkinter.Toplevel()
    root_8.title(u"BMI")
    root_8.geometry("480x330")
    root_8.resizable(False, False)

    btn_8_1=tkinter.Button(root_8,text="計算",command=calc_8,font=("",20),width=20)
    btn_8_1.place(x=100,y=110)
    btn_8_2=tkinter.Button(root_8,text="BMIを閉じる",command=root_8.destroy,font=("",15),width=28,height=1,bg="#ffa300")
    btn_8_2.place(x=90,y=270)

    lbl_8_1=tkinter.Label(root_8,text="身長(cm)",font=("",20))
    lbl_8_1.place(x=30,y=20)
    lbl_8_2=tkinter.Label(root_8,text="体重(kg)",font=("",20))
    lbl_8_2.place(x=30,y=60)
    lbl_8_3=tkinter.Label(root_8,text="BMI",font=("",20))
    lbl_8_3.place(x=30,y=180)
    lbl_8_4=tkinter.Label(root_8,text="肥満度",font=("",20))
    lbl_8_4.place(x=30,y=220)

    txt_8_1=tkinter.Entry(root_8,width=20,font=("",20))
    txt_8_1.place(x=150,y=20)
    txt_8_2=tkinter.Entry(root_8,width=20,font=("",20))
    txt_8_2.place(x=150,y=60)
    txt_8_3=tkinter.Entry(root_8,width=20,font=("",20))
    txt_8_3.place(x=150,y=180)
    txt_8_4=tkinter.Entry(root_8,width=20,font=("",20))
    txt_8_4.place(x=150,y=220)

    root_8.mainloop()
