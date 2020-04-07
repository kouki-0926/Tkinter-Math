import tkinter
from functools import partial
from calculation import *
from sympy import *

#main_window
def main_window():
    root=tkinter.Tk()
    root.title(u"math")
    root.geometry("600x320")
    root.resizable(False, False)

    btn_1=tkinter.Button(root,text="微分",command=sub_window_1,width=20,height=4)
    btn_1.place(x=0,y=30)
    btn_2=tkinter.Button(root,text="積分",command=sub_window_2,width=20,height=4)
    btn_2.place(x=150,y=30)
    btn_3=tkinter.Button(root,text="因数分解",command=sub_window_3,width=20,height=4)
    btn_3.place(x=300,y=30)
    btn_4=tkinter.Button(root,text="方程式",command=sub_window_4,width=20,height=4)
    btn_4.place(x=450,y=30)
    btn_5=tkinter.Button(root,text="テーラー展開",command=sub_window_5,width=20,height=4)
    btn_5.place(x=0,y=105)
    btn_6=tkinter.Button(root,text="階乗",command=sub_window_6,width=20,height=4)
    btn_6.place(x=150,y=105)
    btn_7=tkinter.Button(root,text="連立方程式",command=sub_window_7,width=20,height=4)
    btn_7.place(x=300,y=105)
    btn_8=tkinter.Button(root,text="BMI",command=sub_window_8,width=20,height=4)
    btn_8.place(x=450,y=105)
    btn_9=tkinter.Button(root,text="極限",command=sub_window_9,width=20,height=4)
    btn_9.place(x=0,y=180)
    btn_10=tkinter.Button(root,text="行列",command=sub_window_10,width=20,height=4)
    btn_10.place(x=150,y=180)
    btn_11=tkinter.Button(root,text="行列２",command=sub_window_11,width=20,height=4)
    btn_11.place(x=300,y=180)
    btn_12=tkinter.Button(root,text="進数変換",command=sub_window_12,width=20,height=4)
    btn_12.place(x=450,y=180)
    btn_d=tkinter.Button(root,text="mathを閉じる",command=root.destroy,width=84,height=2,bg="#ffa300")
    btn_d.place(x=0,y=255)

    root.mainloop()

#微分   test038.py
def sub_window_1():
    def calc_1():
        try:
            formula=txt_1_1.get()
            a=txt_1_3.get()

            anser=derivative.derivative(formula,a)
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

#積分　　test046.py
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

#因数分解　test064.py
def sub_window_3():
    def calc_3():
        try:
            formula=txt_3_1.get()

            anser=factorization.factorization(formula)
        except:
            anser="Error"
        txt_3_2.delete(0,tkinter.END)
        txt_3_2.insert(0,anser)

    root_3=tkinter.Toplevel()
    root_3.title(u"因数分解")
    root_3.geometry("1000x300")
    root_3.resizable(False, False)

    btn_3_1=tkinter.Button(root_3,text="計算",command=calc_3,width=40,height=3)
    btn_3_1.place(x=330,y=110)
    btn_3_2=tkinter.Button(root_3,text="因数分解を閉じる",command=root_3.destroy,width=40,height=2,bg="#ffa300")
    btn_3_2.place(x=330,y=240)

    txt_3_1=tkinter.Entry(root_3,width=40,font=("",30))
    txt_3_1.place(x=70,y=50)
    txt_3_2=tkinter.Entry(root_3,width=40,font=("",30))
    txt_3_2.place(x=70,y=180)

    lbl_3_1=tkinter.Label(root_3,text="因数分解したい式を入力してください",font=("",15))
    lbl_3_1.place(x=330,y=20)

    root_3.mainloop()

#方程式　　test044.py
def sub_window_4():
    def calc_4():
        try:
            formula=txt_4_1.get()

            anser=equation.equation(formula)
        except:
            anser=["Error"]
        listbox.delete(0,tkinter.END)
        for i in range(0,len(anser),1):
            listbox.insert(tkinter.END,anser[i])

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

#テーラー展開　　test043.py
def sub_window_5():
    def calc_5():
        try:
            formula=txt_5_1.get()
            dimension=int(txt_5_3.get())
            center=float(txt_5_4.get())
            type=int(txt_5_6.get())
            d=float(txt_5_5.get())

            anser=taylor.taylor(formula,dimension,center,type,d)
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
    lbl_5_1.place(x=790,y=120)
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

#階乗     test049.py
def sub_window_6():
    def calc_6():
        try:
            formula=int(txt_6_1.get())

            anser=Factorial.Factorial(formula)
        except:
            anser="Error"
        txt_6_2.delete(0,tkinter.END)
        txt_6_2.insert(0,anser)

    root_6=tkinter.Toplevel()
    root_6.title(u"階乗")
    root_6.geometry("440x160")
    root_6.resizable(False, False)

    txt_6_1=tkinter.Entry(root_6,width=3,font=("",30))
    txt_6_1.place(x=20,y=20)
    txt_6_2=tkinter.Entry(root_6,width=13,font=("",30))
    txt_6_2.place(x=150,y=20)

    lbl_6_1=tkinter.Label(root_6,text="!  =",font=("",30))
    lbl_6_1.place(x=90,y=20)

    btn_6_1=tkinter.Button(root_6,width=35,height=2,text="計算",command=calc_6)
    btn_6_1.place(x=100,y=70)
    btn_6_2=tkinter.Button(root_6,width=35,height=1,text="階乗を閉じる",command=root_6.destroy,bg="#ffa300")
    btn_6_2.place(x=100,y=120)

    root_6.mainloop()

#連立方程式　test065.py
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
                anser="Error"
            txt_7_2_a.delete(0,tkinter.END)
            txt_7_2_a.insert(0,anser)

        width=1000
        height=a*40+230
        root_7_2=tkinter.Toplevel()
        root_7_2.title(u"連立方程式")
        root_7_2.geometry(f"{width}x{height}")
        root_7_2.resizable(False, False)

        btn_7_2_1=tkinter.Button(root_7_2,text="計算",width=20,command=calc_7_2,font=("",20))
        btn_7_2_1.place(x=380,y=a*45+45)
        btn_7_2_2=tkinter.Button(root_7_2,text="連立方程式を閉じる",width=20,command=root_7_2.destroy,font=("",20),bg="#ffa300")
        btn_7_2_2.place(x=380,y=a*45+150)

        lbl_7_2_1=[]
        lbl_7_2_2=[]
        for i in range(0,int(a),1):
            lbl_7_2_1.append(tkinter.Label(root_7_2,text="式{}".format(i+1),font=("",30)))
            lbl_7_2_1[i].place(x=0,y=i*45+30)
            lbl_7_2_2.append(tkinter.Label(root_7_2,text="=0",font=("",30)))
            lbl_7_2_2[i].place(x=930,y=i*45+30)

        lbl_7_2_a=tkinter.Label(root_7_2,text="解",font=("",30))
        lbl_7_2_a.place(x=10,y=a*45+100)

        txt_7_2_1=[]
        for i in range(0,int(a),1):
            txt_7_2_1.append(tkinter.Entry(root_7_2,width=42,font=("",30)))
            txt_7_2_1[i].place(x=80,y=i*45+30)

        txt_7_2_a=tkinter.Entry(root_7_2,width=42,font=("",30))
        txt_7_2_a.place(x=80,y=a*45+100)

        root_7_2.mainloop()

    sub_window_7_1()

#BMI    test030.py
def sub_window_8():
    def calc_8():
        try:
            height=float(txt_8_1.get())
            weight=float(txt_8_2.get())

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

#極限　　test067.py
def sub_window_9():
    def calc_9():
        try:
            formula=txt_9_1.get()
            a=txt_9_3.get()

            anser=lim.lim(formula,a)
        except:
            anser="Error"
        txt_9_2.delete(0,tkinter.END)
        txt_9_2.insert(0,anser)

    root_9=tkinter.Toplevel()
    root_9.title(u"極限")
    root_9.geometry("960x200")
    root_9.resizable(False, False)

    btn_9_1=tkinter.Button(root_9,text="計算",command=calc_9,width=40,height=2)
    btn_9_1.place(x=330,y=110)
    btn_9_2=tkinter.Button(root_9,text="極限を閉じる",command=root_9.destroy,width=40,height=1,bg="#ffa300")
    btn_9_2.place(x=330,y=155)

    lbl_9_1=tkinter.Label(root_9,text="lim",font=("",40))
    lbl_9_1.place(x=20,y=20)
    lbl_9_2=tkinter.Label(root_9,text="X →",font=("",15))
    lbl_9_2.place(x=20,y=80)
    lbl_9_3=tkinter.Label(root_9,text="=",font=("",50))
    lbl_9_3.place(x=650,y=30)

    txt_9_1=tkinter.Entry(root_9,width=16,font=("",50))
    txt_9_1.place(x=100,y=30)
    txt_9_2=tkinter.Entry(root_9,width=7,font=("",50))
    txt_9_2.place(x=700,y=30)
    txt_9_3=tkinter.Entry(root_9,width=2,font=("",15))
    txt_9_3.place(x=65,y=80)

    txt_9_3.insert(0,0)

    root_9.mainloop()

#行列　　test074.py
def sub_window_10():
    def calc_10(c):
        try:
            Ar=int(txt_10_3.get())
            Ac=int(txt_10_4.get())
            LIST=[]
            for i in range(1,Ar+1,1):
                list=[]
                for j in range(0,Ac,1):
                    m_1=txt_10_1.get(f"{i}.{3*j}")
                    m_2=txt_10_1.get(f"{i}.{3*j+1}")
                    m=int(m_2)
                    if m_1==" ":
                        m=m
                    elif m_1=="-":
                        m=-m
                    list.append(m)
                LIST.append(list)
            A=Matrix(LIST)

            anser=matrix.calculation(A,Ar,Ac,c)

            txt_10_5.delete(0,tkinter.END)
            txt_10_5.insert(0,anser[3])
            txt_10_2.delete("0.end",tkinter.END)
            if anser[4]==0:
                for k in range(0,anser[1],1):
                    B=str(anser[0].row(k))
                    C=B.replace("Matrix","").replace("**","^").replace("*","").replace("([[","[").replace("]])","]\n")
                    txt_10_2.insert(f"{k+1}.{0}",C)
            elif anser[4]==1:
                txt_10_2.insert("1.0",anser[0])
        except:
            txt_10_2.delete("0.end",tkinter.END)
            txt_10_2.insert("0.0","Error")
    root_10=tkinter.Toplevel()
    root_10.title(u"行列")
    root_10.geometry("1400x500")
    root_10.resizable(False, False)

    btn_10_1=tkinter.Button(root_10,text="行列を閉じる",width=30,command=root_10.destroy,font=("",15),bg="#ffa300")
    btn_10_1.place(x=1030,y=460)
    btn_10_2=tkinter.Button(root_10,text="A",command=partial(calc_10,0),width=30,font=("",15))
    btn_10_2.place(x=1030,y=20)
    btn_10_3=tkinter.Button(root_10,text="n乗",command=partial(calc_10,1),width=30,font=("",15))
    btn_10_3.place(x=1030,y=60)
    btn_10_4=tkinter.Button(root_10,text="転置",command=partial(calc_10,2),width=30,font=("",15))
    btn_10_4.place(x=1030,y=100)
    btn_10_5=tkinter.Button(root_10,text="逆行列",command=partial(calc_10,3),width=30,font=("",15))
    btn_10_5.place(x=1030,y=140)
    btn_10_6=tkinter.Button(root_10,text="余因子行列",command=partial(calc_10,4),width=30,font=("",15))
    btn_10_6.place(x=1030,y=180)
    btn_10_7=tkinter.Button(root_10,text="行列式",command=partial(calc_10,5),width=30,font=("",15))
    btn_10_7.place(x=1030,y=220)
    btn_10_8=tkinter.Button(root_10,text="階数",command=partial(calc_10,6),width=30,font=("",15))
    btn_10_8.place(x=1030,y=260)
    btn_10_9=tkinter.Button(root_10,text="トレース",command=partial(calc_10,7),width=30,font=("",15))
    btn_10_9.place(x=1030,y=300)
    btn_10_10=tkinter.Button(root_10,text="固有値",command=partial(calc_10,8),width=30,font=("",15))
    btn_10_10.place(x=1030,y=340)
    btn_10_11=tkinter.Button(root_10,text="対角化行列",command=partial(calc_10,9),width=30,font=("",15))
    btn_10_11.place(x=1030,y=380)
    btn_10_12=tkinter.Button(root_10,text="対角行列",command=partial(calc_10,10),width=30,font=("",15))
    btn_10_12.place(x=1030,y=420)

    lbl_10_1=tkinter.Label(root_10,text="A:",font=("",20))
    lbl_10_1.place(x=0,y=95)
    lbl_10_2=tkinter.Label(root_10,text="行",font=("",20))
    lbl_10_2.place(x=65,y=95)
    lbl_10_3=tkinter.Label(root_10,text="列",font=("",20))
    lbl_10_3.place(x=135,y=95)
    lbl_10_4=tkinter.Label(root_10,text="↓",font=("",38))
    lbl_10_4.place(x=580,y=220)
    lbl_10_5=tkinter.Label(root_10,text="A=",font=("",40))
    lbl_10_5.place(x=200,y=80)
    lbl_10_6=tkinter.Label(root_10,text="=",font=("",40))
    lbl_10_6.place(x=230,y=350)

    txt_10_1=tkinter.Text(root_10,width=50,height=7,font=("",20))
    txt_10_1.place(x=270,y=20)
    txt_10_2=tkinter.Text(root_10,width=50,height=7,font=("",20))
    txt_10_2.place(x=270,y=280)
    txt_10_3=tkinter.Entry(root_10,width=2,font=("",20))
    txt_10_3.place(x=30,y=95)
    txt_10_4=tkinter.Entry(root_10,width=2,font=("",20))
    txt_10_4.place(x=100,y=95)
    txt_10_5=tkinter.Entry(root_10,width=8,font=("",40))
    txt_10_5.place(x=10,y=350)

    txt_10_3.insert(0,"2")
    txt_10_4.insert(0,"2")

    root_10.mainloop()

#行列2　test075.py
def sub_window_11():
    def calc_11(type):
        try:
            Ar=int(txt_11_4.get())
            Ac=int(txt_11_5.get())
            LIST=[]
            for i in range(1,Ar+1,1):
                list=[]
                for j in range(0,Ac,1):
                    m_1=txt_11_1.get(f"{i}.{3*j}")
                    m_2=txt_11_1.get(f"{i}.{3*j+1}")
                    m=int(m_2)
                    if m_1==" ":
                        m=m
                    elif m_1=="-":
                        m=-m
                    list.append(m)
                LIST.append(list)
            A=Matrix(LIST)

            Br=int(txt_11_6.get())
            Bc=int(txt_11_7.get())
            LIST=[]
            for i in range(1,Br+1,1):
                list=[]
                for j in range(0,Bc,1):
                    m_1=txt_11_2.get(f"{i}.{3*j}")
                    m_2=txt_11_2.get(f"{i}.{3*j+1}")
                    m=int(m_2)
                    if m_1==" ":
                        m=m
                    elif m_1=="-":
                        m=-m
                    list.append(m)
                LIST.append(list)
            B=Matrix(LIST)

            k=int(txt_11_8.get())
            l=int(txt_11_9.get())

            anser=matrix_2.calculation(A,B,Ar,Ac,Br,Bc,type,k,l)

            txt_11_10.delete(0,tkinter.END)
            txt_11_10.insert(0,anser[1])
            txt_11_3.delete("0.end",tkinter.END)
            for k in range(0,anser[2],1):
                B=str(anser[0].row(k))
                C=B.replace("Matrix","").replace("**","^").replace("*","").replace("([[","[").replace("]])","]\n")
                txt_11_3.insert(f"{k+1}.{0}",C)
        except:
            txt_11_3.delete("0.end",tkinter.END)
            txt_11_3.insert("0.0","Error")


    root_11=tkinter.Toplevel()
    root_11.title(u"行列2")
    root_11.geometry("1400x500")
    root_11.resizable(False, False)

    btn_11_1=tkinter.Button(root_11,text="行列2を閉じる",width=30,command=root_11.destroy,font=("",15),bg="#ffa300")
    btn_11_1.place(x=1030,y=460)
    btn_11_2=tkinter.Button(root_11,text="A",command=partial(calc_11,0),width=30,font=("",15))
    btn_11_2.place(x=1030,y=260)
    btn_11_3=tkinter.Button(root_11,text="B",command=partial(calc_11,1),width=30,font=("",15))
    btn_11_3.place(x=1030,y=300)
    btn_11_4=tkinter.Button(root_11,text="kA+lB",command=partial(calc_11,2),width=30,font=("",15))
    btn_11_4.place(x=1030,y=340)
    btn_11_5=tkinter.Button(root_11,text="AB",command=partial(calc_11,3),width=30,font=("",15))
    btn_11_5.place(x=1030,y=380)
    btn_11_6=tkinter.Button(root_11,text="BA",command=partial(calc_11,4),width=30,font=("",15))
    btn_11_6.place(x=1030,y=420)

    lbl_11_1=tkinter.Label(root_11,text="A:",font=("",20))
    lbl_11_1.place(x=0,y=70)
    lbl_11_2=tkinter.Label(root_11,text="行",font=("",20))
    lbl_11_2.place(x=65,y=70)
    lbl_11_3=tkinter.Label(root_11,text="列",font=("",20))
    lbl_11_3.place(x=145,y=70)
    lbl_11_4=tkinter.Label(root_11,text="B:",font=("",20))
    lbl_11_4.place(x=0,y=110)
    lbl_11_5=tkinter.Label(root_11,text="行",font=("",20))
    lbl_11_5.place(x=65,y=110)
    lbl_11_6=tkinter.Label(root_11,text="列",font=("",20))
    lbl_11_6.place(x=145,y=110)
    lbl_11_7=tkinter.Label(root_11,text="↓",font=("",38))
    lbl_11_7.place(x=580,y=220)
    lbl_11_8=tkinter.Label(root_11,text="A=",font=("",40))
    lbl_11_8.place(x=200,y=80)
    lbl_11_9=tkinter.Label(root_11,text="=",font=("",40))
    lbl_11_9.place(x=230,y=350)
    lbl_11_10=tkinter.Label(root_11,text="B=",font=("",40))
    lbl_11_10.place(x=800,y=80)
    lbl_11_11=tkinter.Label(root_11,text="k",font=("",20))
    lbl_11_11.place(x=5,y=150)
    lbl_11_12=tkinter.Label(root_11,text="l",font=("",20))
    lbl_11_12.place(x=85,y=150)

    txt_11_1=tkinter.Text(root_11,width=35,height=7,font=("",20))
    txt_11_1.place(x=270,y=20)
    txt_11_2=tkinter.Text(root_11,width=35,height=7,font=("",20))
    txt_11_2.place(x=870,y=20)
    txt_11_3=tkinter.Text(root_11,width=50,height=7,font=("",20))
    txt_11_3.place(x=270,y=280)
    txt_11_4=tkinter.Entry(root_11,width=2,font=("",20))
    txt_11_4.place(x=30,y=70)
    txt_11_5=tkinter.Entry(root_11,width=2,font=("",20))
    txt_11_5.place(x=110,y=70)
    txt_11_6=tkinter.Entry(root_11,width=2,font=("",20))
    txt_11_6.place(x=30,y=110)
    txt_11_7=tkinter.Entry(root_11,width=2,font=("",20))
    txt_11_7.place(x=110,y=110)
    txt_11_8=tkinter.Entry(root_11,width=2,font=("",20))
    txt_11_8.place(x=30,y=150)
    txt_11_9=tkinter.Entry(root_11,width=2,font=("",20))
    txt_11_9.place(x=110,y=150)
    txt_11_10=tkinter.Entry(root_11,width=8,font=("",40))
    txt_11_10.place(x=10,y=350)

    txt_11_4.insert(0,"2")
    txt_11_5.insert(0,"2")
    txt_11_6.insert(0,"2")
    txt_11_7.insert(0,"2")
    txt_11_8.insert(0,"2")
    txt_11_9.insert(0,"2")

    root_11.mainloop()

#進数変換　test078.py
def sub_window_12():
    def calc_12():
        try:
            if txt_1.get()!="":
                base="binary"
                before_conversion=txt_1.get()
            elif txt_2.get()!="":
                base="octal"
                before_conversion=txt_2.get()
            elif txt_3.get()!="":
                base="decimal"
                before_conversion=txt_3.get()
            elif txt_4.get()!="":
                base="hexadecimal"
                before_conversion=txt_4.get()

            anser=base_conversion.base_conversion(base,before_conversion)
        except:
            anser=["Error","Error","Error","Error"]

        txt_1.delete(0,tkinter.END)
        txt_1.insert(0,anser[0])
        txt_2.delete(0,tkinter.END)
        txt_2.insert(0,anser[1])
        txt_3.delete(0,tkinter.END)
        txt_3.insert(0,anser[2])
        txt_4.delete(0,tkinter.END)
        txt_4.insert(0,anser[3])

    def dele():
        txt_1.delete(0,tkinter.END)
        txt_2.delete(0,tkinter.END)
        txt_3.delete(0,tkinter.END)
        txt_4.delete(0,tkinter.END)

    root_12=tkinter.Toplevel()
    root_12.title(u"進数変換")
    root_12.geometry("430x330")
    root_12.resizable(False, False)

    btn_1=tkinter.Button(root_12,text="進数変換を閉じる",width=34,command=root_12.destroy,font=("",15),bg="#ffa300")
    btn_1.place(x=20,y=270)
    btn_2=tkinter.Button(root_12,text="計算",command=calc_12,width=34,font=("",15))
    btn_2.place(x=20,y=180)
    btn_3=tkinter.Button(root_12,text="全削除",command=dele,width=34,font=("",15))
    btn_3.place(x=20,y=220)

    lbl_1=tkinter.Label(root_12,text="２進数",font=("",20))
    lbl_1.place(x=20,y=20)
    lbl_2=tkinter.Label(root_12,text="８進数",font=("",20))
    lbl_2.place(x=20,y=60)
    lbl_3=tkinter.Label(root_12,text="１０進数",font=("",20))
    lbl_3.place(x=10,y=100)
    lbl_4=tkinter.Label(root_12,text="１６進数",font=("",20))
    lbl_4.place(x=10,y=140)

    txt_1=tkinter.Entry(root_12,font=("",20))
    txt_1.place(x=120,y=20)
    txt_2=tkinter.Entry(root_12,font=("",20))
    txt_2.place(x=120,y=60)
    txt_3=tkinter.Entry(root_12,font=("",20))
    txt_3.place(x=120,y=100)
    txt_4=tkinter.Entry(root_12,font=("",20))
    txt_4.place(x=120,y=140)

    root_12.mainloop()
