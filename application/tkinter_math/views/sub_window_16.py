import tkinter
from tkinter_math.calculation import *

def sub_window_16():
    def calc_16():
        try:
            N=txt_16_1.get()
            anser=Sieve_of_Eratosthenes.Sieve_of_Eratosthenes(N)
        except:
            anser=["Error"]
        txt_16_2.delete("0.end",tkinter.END)
        txt_16_2.insert("0.0",anser)

    root_16=tkinter.Toplevel()
    root_16.title(u"ソクラテスのふるい")
    root_16.geometry("850x650")
    root_16.resizable(False, False)

    btn_16_1=tkinter.Button(root_16,text="計算",command=calc_16,width=40,height=3)
    btn_16_1.place(x=280,y=110)
    btn_16_2=tkinter.Button(root_16,text="ソクラテスのふるいを閉じる",command=root_16.destroy,width=40,height=2,bg="#ffa300")
    btn_16_2.place(x=280,y=600)

    txt_16_1=tkinter.Entry(root_16,width=40,font=("",30))
    txt_16_1.place(x=20,y=50)
    txt_16_2=tkinter.Text(root_16,width=40,height=10,font=("",30))
    txt_16_2.place(x=20,y=180)

    lbl_16_1=tkinter.Label(root_16,text="整数を入力してください",font=("",15))
    lbl_16_1.place(x=330,y=20)

    root_16.mainloop()
