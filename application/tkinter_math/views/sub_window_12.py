import tkinter
from tkinter_math.calculation import *

def sub_window_12():
    def calc_12():
        try:
            if txt_12_1.get()!="":
                base="binary"
                before_conversion=txt_12_1.get()
            elif txt_12_2.get()!="":
                base="octal"
                before_conversion=txt_12_2.get()
            elif txt_12_3.get()!="":
                base="decimal"
                before_conversion=txt_12_3.get()
            elif txt_12_4.get()!="":
                base="hexadecimal"
                before_conversion=txt_12_4.get()
            anser=base_conversion.base_conversion(base,before_conversion)
        except:
            anser=["Error","Error","Error","Error"]
        dele()
        txt_12_1.insert(0,anser[0])
        txt_12_2.insert(0,anser[1])
        txt_12_3.insert(0,anser[2])
        txt_12_4.insert(0,anser[3])

    def dele():
        txt_12_1.delete(0,tkinter.END)
        txt_12_2.delete(0,tkinter.END)
        txt_12_3.delete(0,tkinter.END)
        txt_12_4.delete(0,tkinter.END)

    root_12=tkinter.Toplevel()
    root_12.title(u"進数変換")
    root_12.geometry("430x330")
    root_12.resizable(False, False)

    btn_12_1=tkinter.Button(root_12,text="進数変換を閉じる",width=34,command=root_12.destroy,font=("",15),bg="#ffa300")
    btn_12_1.place(x=20,y=270)
    btn_12_2=tkinter.Button(root_12,text="計算",command=calc_12,width=34,font=("",15))
    btn_12_2.place(x=20,y=180)
    btn_12_3=tkinter.Button(root_12,text="全削除",command=dele,width=34,font=("",15))
    btn_12_3.place(x=20,y=220)

    lbl_12_1=tkinter.Label(root_12,text="２進数",font=("",20))
    lbl_12_1.place(x=20,y=20)
    lbl_12_2=tkinter.Label(root_12,text="８進数",font=("",20))
    lbl_12_2.place(x=20,y=60)
    lbl_12_3=tkinter.Label(root_12,text="１０進数",font=("",20))
    lbl_12_3.place(x=10,y=100)
    lbl_12_4=tkinter.Label(root_12,text="１６進数",font=("",20))
    lbl_12_4.place(x=10,y=140)

    txt_12_1=tkinter.Entry(root_12,font=("",20))
    txt_12_1.place(x=120,y=20)
    txt_12_2=tkinter.Entry(root_12,font=("",20))
    txt_12_2.place(x=120,y=60)
    txt_12_3=tkinter.Entry(root_12,font=("",20))
    txt_12_3.place(x=120,y=100)
    txt_12_4=tkinter.Entry(root_12,font=("",20))
    txt_12_4.place(x=120,y=140)

    root_12.mainloop()
