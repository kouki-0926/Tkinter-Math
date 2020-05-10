import tkinter
from tkinter_math.calculation import *

def sub_window_4():
    def calc_4():
        try:
            formula=txt_4_1.get()
            anser=equation.equation(formula)
            listbox.delete(0,tkinter.END)
            for i in range(0,len(anser),1):
                listbox.insert(tkinter.END,anser[i])
        except:
            anser=["Error"]

    root_4=tkinter.Toplevel()
    root_4.title(u"方程式")
    root_4.geometry("950x630")
    root_4.resizable(False, False)

    btn_4_1=tkinter.Button(root_4,text="方程式を閉じる",command=root_4.destroy,font=("",15),width=20,bg="#ffa300")
    btn_4_1.place(x=360,y=570)
    btn_4_2=tkinter.Button(root_4,text="計算",command=calc_4,font=("",30),width=20)
    btn_4_2.place(x=260,y=120)

    lbl_4_1=tkinter.Label(root_4,text="方程式を入力してください",font=("",20))
    lbl_4_1.place(x=0,y=20)
    lbl_4_2=tkinter.Label(root_4,text="解",font=("",20))
    lbl_4_2.place(x=10,y=350)
    lbl_4_3=tkinter.Label(root_4,text="=0",font=("",30))
    lbl_4_3.place(x=860,y=50)

    txt_4_1=tkinter.Entry(root_4,width=40,font=("",30))
    txt_4_1.place(x=50,y=50)

    scrollbar_frame = tkinter.Frame(root_4)
    scrollbar_frame.grid(padx=50, pady=220)
    listbox = tkinter.Listbox(scrollbar_frame,height=8,width=42,font=("",30))
    listbox.pack(side=tkinter.LEFT)
    yscroll_bar =tkinter.Scrollbar(scrollbar_frame, command=listbox.yview)
    yscroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    listbox.config(yscrollcommand=yscroll_bar.set)

    root_4.mainloop()
