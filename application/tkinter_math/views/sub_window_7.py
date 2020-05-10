import tkinter
from tkinter_math.calculation import *

def sub_window_7():
    def sub_window_7_1():
        def calc_7_1():
            try:
                a=int(txt_7_1_1.get())
                root_7_1.destroy()
                sub_window_7_2(a)
            except:
                lbl_7_1_2=tkinter.Label(root_7_1,text="Error",font=("",15),fg="#ff0000")
                lbl_7_1_2.place(x=200,y=0)
        root_7_1=tkinter.Toplevel()
        root_7_1.title(u"連立方程式")
        root_7_1.geometry("400x180")
        root_7_1.resizable(False, False)

        btn_7_1_1=tkinter.Button(root_7_1,text="実行",command=calc_7_1,width=40,height=3)
        btn_7_1_1.place(x=50,y=80)
        btn_7_1_2=tkinter.Button(root_7_1,text="連立方程式を閉じる",command=root_7_1.destroy,width=40,height=1,bg="#ffa300")
        btn_7_1_2.place(x=50,y=140)

        lbl_7_1_1=tkinter.Label(root_7_1,text="式の数を入力してください",font=("",15))
        lbl_7_1_1.place(x=20,y=30)

        txt_7_1_1=tkinter.Entry(root_7_1,width=4,font=("",30))
        txt_7_1_1.place(x=270,y=25)

        root_7_1.mainloop()

    def sub_window_7_2(a):
        def calc_7_2():
            try:
                formura=[]
                for i in range(0,int(a),1):
                    formura.append(txt_7_2_1[i].get())

                anser=equations.equations(formura)
            except:
                anser=["Error"]
            listbox.delete(0,tkinter.END)
            for i in range(0,len(anser),1):
                listbox.insert(tkinter.END,anser[i])

        width=1000
        height=a*40+550
        root_7_2=tkinter.Toplevel()
        root_7_2.title(u"連立方程式")
        root_7_2.geometry(f"{width}x{height}")
        root_7_2.resizable(False, False)

        btn_7_2_1=tkinter.Button(root_7_2,text="計算",width=20,command=calc_7_2,font=("",20))
        btn_7_2_1.place(x=380,y=a*45+45)
        btn_7_2_2=tkinter.Button(root_7_2,text="連立方程式を閉じる",width=20,command=root_7_2.destroy,font=("",20),bg="#ffa300")
        btn_7_2_2.place(x=380,y=a*45+450)

        lbl_7_2_1=[]
        lbl_7_2_2=[]
        for i in range(0,int(a),1):
            lbl_7_2_1.append(tkinter.Label(root_7_2,text="式{}".format(i+1),font=("",30)))
            lbl_7_2_1[i].place(x=0,y=i*45+30)
            lbl_7_2_2.append(tkinter.Label(root_7_2,text="=0",font=("",30)))
            lbl_7_2_2[i].place(x=930,y=i*45+30)

        lbl_7_2_a=tkinter.Label(root_7_2,text="解",font=("",30))
        lbl_7_2_a.place(x=10,y=a*45+250)

        txt_7_2_1=[]
        for i in range(0,int(a),1):
            txt_7_2_1.append(tkinter.Entry(root_7_2,width=42,font=("",30)))
            txt_7_2_1[i].place(x=80,y=i*45+30)

        scrollbar_frame = tkinter.Frame(root_7_2)
        scrollbar_frame.grid(padx=80, pady=a*45+100)
        listbox = tkinter.Listbox(scrollbar_frame,height=8,width=42,font=("",30))
        listbox.pack(side=tkinter.LEFT)
        yscroll_bar =tkinter.Scrollbar(scrollbar_frame, command=listbox.yview)
        yscroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        listbox.config(yscrollcommand=yscroll_bar.set)

        root_7_2.mainloop()

    sub_window_7_1()
