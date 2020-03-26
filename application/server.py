import tkinter
from functools import partial
from calculation import *

#import sys
#import math
from sympy import *

#main_window
def main_window():
    root=tkinter.Tk()
    root.title(u"math")
    root.geometry("600x290")
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
    btn_11=tkinter.Button(root,text="",width=20,height=4)
    btn_11.place(x=300,y=180)
    btn_d=tkinter.Button(root,text="mathを閉じる",command=root.destroy,width=20,height=4,bg="#ffa300")
    btn_d.place(x=450,y=180)

    root.mainloop()

#微分   test038.py
def sub_window_1():
    def calc_1():
        formula=txt_1_1.get()
        a=txt_1_3.get()

        anser=derivative.derivative(formula,a)
        txt_1_2.delete(0,tkinter.END)
        txt_1_2.insert(0,anser)

    root_1=tkinter.Toplevel()
    root_1.title(u"微分")
    root_1.geometry("1500x300")
    root_1.resizable(False, False)

    btn_1_1=tkinter.Button(root_1,text="計算",width=20,command=calc_1,font=("",20))
    btn_1_1.place(x=500,y=140)

    txt_1_1=tkinter.Entry(root_1,width=73,font=("",30))
    txt_1_1.place(x=20,y=50)
    txt_1_2=tkinter.Entry(root_1,width=73,font=("",30))
    txt_1_2.place(x=20,y=220)
    txt_1_3=tkinter.Entry(root_1,width=2,font=("",30))
    txt_1_3.place(x=1000,y=140)

    lbl_1_1=tkinter.Label(root_1,text="関数を入力してください",font=("",20))
    lbl_1_1.place(x=20,y=15)
    lbl_1_2=tkinter.Label(root_1,text="導関数",font=("",20))
    lbl_1_2.place(x=20,y=185)

    txt_1_3.insert(0,"x")

    root_1.mainloop()

#積分　　test046.py
def sub_window_2():
    def calc_2():
        formula=txt_2_1.get()
        a=txt_2_2.get()
        b=txt_2_3.get()
        c=int(txt_2_5.get())

        anser=integral.integral(formula,a,b,c)
        txt_2_4.delete(0,tkinter.END)
        txt_2_4.insert(0,anser)

    root_2=tkinter.Toplevel()
    root_2.title(u"積分")
    root_2.geometry("1500x280")
    root_2.resizable(False, False)

    btn_2_1=tkinter.Button(root_2,text="計算",width=20,command=calc_2,font=("",20))
    btn_2_1.place(x=580,y=200)

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
        formula=txt_3_1.get()

        anser=factorization.factorization(formula)
        txt_3_2.delete(0,tkinter.END)
        txt_3_2.insert(0,anser)

    root_3=tkinter.Toplevel()
    root_3.title(u"因数分解")
    root_3.geometry("1000x300")
    root_3.resizable(False, False)

    btn_3_1=tkinter.Button(root_3,text="計算",command=calc_3,width=20,height=3)
    btn_3_1.place(x=400,y=110)
    btn_3_2=tkinter.Button(root_3,text="因数分解を閉じる",command=root_3.destroy,width=20,height=2,bg="#ffa300")
    btn_3_2.place(x=400,y=240)

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
        formula=txt_4_1.get()

        anser=equation.equation(formula)
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
    root_11=tkinter.Toplevel()
    root_11.title(u"テーラー展開")
    root_11.geometry("600x400")
    root_11.resizable(False, False)

    def fx():
        a=txt_11_3.get()
        b=txt_11_4.get()
        b=float(b)
        d=txt_11_6.get()
        d=int(d)

        x = Symbol('x')
        f=txt_11_1.get()
        f=integrate(f)
        f=diff(f)
        A=f.subs(x,b)

        for number in range(1,int(a)+1,1):
            f=diff(f)
            C=f.subs(x,b)/factorial(number)

            if d==1:
                C=C
            else:
                c=txt_11_5.get()
                c=float(c)
                c=10**-c

                if abs(C)<c:
                    C=0
                else:
                    C=C

            A=C*(x-b)**number+A

        A=str(A)
        B=str(txt_11_1.get())+"≒"+str(A.replace("**","B").replace("*","").replace("B","^"))
        C=str(txt_11_1.get())+"≒"+str(A)

        txt_11_2.delete("1.0",tkinter.END)
        txt_11_2.insert("1.0",B)

        print("------------------------------------------------------------------------------------------------------------------------")
        print(B)
        print("")
        print(C)
        print("")



    btn_1=tkinter.Button(root_11,text="計算",command=fx)
    btn_1.place(x=270,y=330)
    btn_2=tkinter.Button(root_11,text="テーラー展開を閉じる",command=root_11.destroy)
    btn_2.place(x=230,y=360)

    txt_11_1=tkinter.Entry(root_11,width=50,font=80)
    txt_11_1.place(x=30,y=30)
    txt_11_2=tkinter.Text(root_11,width=50,height=8,font=80)
    txt_11_2.place(x=30,y=120)
    txt_11_3=tkinter.Entry(root_11,width=3,font=80)
    txt_11_3.place(x=200,y=70)
    txt_11_4=tkinter.Entry(root_11,width=3,font=80)
    txt_11_4.place(x=280,y=70)
    txt_11_5=tkinter.Entry(root_11,width=3,font=80)
    txt_11_5.place(x=550,y=70)
    txt_11_6=tkinter.Entry(root_11,width=3,font=80)
    txt_11_6.place(x=500,y=70)

    lbl_11_1=tkinter.Label(root_11,text="べき乗")
    lbl_11_1.place(x=160,y=70)
    lbl_11_2=tkinter.Label(root_11,text="x=")
    lbl_11_2.place(x=255,y=70)
    lbl_11_3=tkinter.Label(root_11,text="周り")
    lbl_11_3.place(x=320,y=70)
    lbl_11_4=tkinter.Label(root_11,text="関数")
    lbl_11_4.place(x=0,y=30)

    txt_11_3.insert(0,50)
    txt_11_4.insert(0,0)
    txt_11_5.insert(0,15)
    txt_11_6.insert(0,1)

    root_11.mainloop()

#階乗     test049.py
def sub_window_6():
    root_12=tkinter.Toplevel()
    root_12.title(u"階乗")
    root_12.geometry("440x160")
    root_12.resizable(False, False)

    def x():
        a=txt_1.get()
        b=math.factorial(int(a))
        txt_2.delete(0,tkinter.END)
        txt_2.insert(0,str(b))


    txt_1=tkinter.Entry(root_12,width=3,font=("",30))
    txt_1.place(x=20,y=20)
    txt_2=tkinter.Entry(root_12,width=13,font=("",30))
    txt_2.place(x=150,y=20)

    lbl_1=tkinter.Label(root_12,text="!  =",font=("",30))
    lbl_1.place(x=90,y=20)

    btn_1=tkinter.Button(root_12,width=35,height=2,text="計算",command=x)
    btn_1.place(x=100,y=70)
    btn_2=tkinter.Button(root_12,width=35,text="階乗を閉じる",command=root_12.destroy)
    btn_2.place(x=100,y=120)

    root_12.mainloop()

#連立方程式　test065.py
def sub_window_7():
    def sub_window_7_1():
        root_7_1=tkinter.Toplevel()
        root_7_1.title(u"連立方程式")
        root_7_1.geometry("400x180")
        root_7_1.resizable(False, False)

        def sub():
            a=txt_1.get()
            a=int(a)
            root_7_1.destroy()
            sub_window_7_2(a)

        btn_1=tkinter.Button(root_7_1,text="実行",command=sub,width=40,height=3)
        btn_1.place(x=50,y=80)
        btn_2=tkinter.Button(root_7_1,text="連立方程式を閉じる",command=root_7_1.destroy,width=40,height=1)
        btn_2.place(x=50,y=140)

        lbl_1=tkinter.Label(root_7_1,text="式の数を入力してください",font=10)
        lbl_1.place(x=20,y=30)

        txt_1=tkinter.Entry(root_7_1,width=4,font=("",30))
        txt_1.place(x=270,y=25)

        root_7_1.mainloop()

    def sub_window_7_2(a):
        width=1000
        height=a*40+230
        root_7_2=tkinter.Toplevel()
        root_7_2.title(u"連立方程式")
        root_7_2.geometry(f"{width}x{height}")
        root_7_2.resizable(False, False)

        def fa():
            formura=[]
            for i in range(0,int(a),1):
                formura.append(txt_2_1[i].get())

            A=solve(formura)

            txt_2_a.delete(0,tkinter.END)
            txt_2_a.insert(0,A)



        btn_2_1=tkinter.Button(root_7_2,text="計算",width=20,command=fa,font=10)
        btn_2_1.place(x=380,y=a*45+50)
        btn_2_2=tkinter.Button(root_7_2,text="連立方程式を閉じる",width=20,command=root_7_2.destroy,font=10)
        btn_2_2.place(x=380,y=a*45+150)


        lbl_2_1=[]
        lbl_2_2=[]
        for i in range(0,int(a),1):
            lbl_2_1.append(tkinter.Label(root_7_2,text="式{}".format(i+1),font=("",30)))
            lbl_2_1[i].place(x=0,y=i*45+30)
            lbl_2_2.append(tkinter.Label(root_7_2,text="=0",font=("",30)))
            lbl_2_2[i].place(x=930,y=i*45+30)

        lbl_2_a=tkinter.Label(root_7_2,text="解",font=("",30))
        lbl_2_a.place(x=10,y=a*45+100)


        txt_2_1=[]
        for i in range(0,int(a),1):
            txt_2_1.append(tkinter.Entry(root_7_2,width=42,font=("",30)))
            txt_2_1[i].place(x=80,y=i*45+30)

        txt_2_a=tkinter.Entry(root_7_2,width=42,font=("",30))
        txt_2_a.place(x=80,y=a*45+100)

        root_7_2.mainloop()

    sub_window_7_1()

#BMI    test030.py
def sub_window_8():
    root_7=tkinter.Toplevel()
    root_7.title(u"BMI")
    root_7.geometry("300x330")
    root_7.resizable(False, False)

    btn_6_1=tkinter.Button(root_7,text="BMIを閉じる",command=root_7.destroy)
    btn_6_1.place(x=120,y=300)

    lbl_1=tkinter.Label(root_7,text="身長(cm)")
    lbl_1.place(x=30,y=70)
    lbl_2=tkinter.Label(root_7,text="体重(kg)")
    lbl_2.place(x=30,y=100)
    lbl_3=tkinter.Label(root_7,text="BMI")
    lbl_3.place(x=30,y=200)
    lbl_4=tkinter.Label(root_7,text="肥満度")
    lbl_4.place(x=30,y=230)

    txt_1=tkinter.Entry(root_7,width=20)
    txt_1.place(x=110,y=70)
    txt_2=tkinter.Entry(root_7,width=20)
    txt_2.place(x=110,y=100)
    txt_3=tkinter.Entry(root_7,width=20)
    txt_3.place(x=110,y=200)
    txt_4=tkinter.Entry(root_7,width=20)
    txt_4.place(x=110,y=230)


    def btn_click():
        txt_3.delete(0,tkinter.END)
        txt_4.delete(0,tkinter.END)

        身長=float(txt_1.get())
        体重=float(txt_2.get())

        BMI=int(体重)*10000/(int(身長)*int(身長))

        txt_3.insert(0,BMI)

        if BMI<18.5:
            txt_4.insert(0,"あなたは低体重です")
        elif BMI>=18.5 and BMI<25:
            txt_4.insert(0,"あなたは普通体重です")
        else:
            txt_4.insert(0,"あなたは肥満です")

    btn=tkinter.Button(root_7,text="計算",command=btn_click)
    btn.place(x=140,y=140)

    root_7.mainloop()

#極限　　test067.py
def sub_window_9():
    root_9=tkinter.Toplevel()
    root_9.title(u"極限")
    root_9.geometry("960x200")
    root_9.resizable(False, False)

    x = Symbol('x')

    def li():
        f = txt_1.get()
        a=txt_3.get()

        A = limit(f, x, a)

        txt_2.delete(0,tkinter.END)
        txt_2.insert(0,A)


    btn_1=tkinter.Button(root_9,text="計算",command=li,width=40,height=2)
    btn_1.place(x=330,y=110)
    btn_2=tkinter.Button(root_9,text="極限を閉じる",command=root_9.destroy,width=40,height=1)
    btn_2.place(x=330,y=155)

    lbl_1=tkinter.Label(root_9,text="lim",font=("",40))
    lbl_1.place(x=20,y=20)
    lbl_2=tkinter.Label(root_9,text="X →",font=("",15))
    lbl_2.place(x=20,y=80)
    lbl_2=tkinter.Label(root_9,text="=",font=("",50))
    lbl_2.place(x=650,y=30)

    txt_1=tkinter.Entry(root_9,width=16,font=("",50))
    txt_1.place(x=100,y=30)
    txt_2=tkinter.Entry(root_9,width=7,font=("",50))
    txt_2.place(x=700,y=30)
    txt_3=tkinter.Entry(root_9,width=2,font=("",15))
    txt_3.place(x=65,y=80)

    txt_3.insert(0,0)

    root_9.mainloop()

#行列　　test074.py
def sub_window_10():
    root_10=tkinter.Toplevel()
    root_10.title(u"行列")
    root_10.geometry("1000x500")
    root_10.resizable(False, False)

    def get(c):
        a=int(txt_10_3.get())
        b=int(txt_10_4.get())

        LIST=[]
        for i in range(1,b+1,1):
            list=[]
            for j in range(0,a,1):
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

        calculation(A,a,b,c)

    def calculation(A,a,b,c):
        d=0
        if c==0:
            A=A
            D="A"

        elif c==1:
            A=A**2
            D="A^2"

        elif c==2:
            A=A.transpose()
            D="A^t"
            b=a

        elif c==3:
            A=A.inv()
            D="A^-1"

        elif c==4:
            A=A.adjugate()
            D="A~"

        elif c==5:
            A=A.det()
            D="det(A)"
            d=1

        elif c==6:
            A=A.rank()
            D="rank(A)"
            d=1

        elif c==7:
            A=A.trace()
            D="tr(A)"
            d=1

        elif c==8:
            A=A.eigenvals()
            A=list(A)
            D="λ"
            d=1

        elif c==9:
            A=A.diagonalize()
            A=list(A)
            A=A[0]
            D="P"

        elif c==10:
            A=A.diagonalize()
            A=list(A)
            A=A[1]
            D="P^-1AP"

        out(A,D,d,b)

    def out(A,D,d,b):
        txt_10_5.delete(0,tkinter.END)
        txt_10_5.insert(0,D)
        txt_10_2.delete("0.end",tkinter.END)
        if d==0:
            for k in range(0,b,1):
                B=str(A.row(k))
                C=B.replace("Matrix","").replace("([[","[").replace("]])","]\n")
                txt_10_2.insert(f"{k+1}.{0}",C)
        elif d==1:
            txt_10_2.insert("1.0",A)


    btn_10_1=tkinter.Button(root_10,text="行列を閉じる",width=30,command=root_10.destroy,font=("",15),bg="#ffa300")
    btn_10_1.place(x=600,y=460)
    btn_10_2=tkinter.Button(root_10,text="A",command=partial(get,0),width=30,font=("",15))
    btn_10_2.place(x=600,y=20)
    btn_10_3=tkinter.Button(root_10,text="２乗",command=partial(get,1),width=30,font=("",15))
    btn_10_3.place(x=600,y=60)
    btn_10_4=tkinter.Button(root_10,text="転置",command=partial(get,2),width=30,font=("",15))
    btn_10_4.place(x=600,y=100)
    btn_10_5=tkinter.Button(root_10,text="逆行列",command=partial(get,3),width=30,font=("",15))
    btn_10_5.place(x=600,y=140)
    btn_10_6=tkinter.Button(root_10,text="余因子行列",command=partial(get,4),width=30,font=("",15))
    btn_10_6.place(x=600,y=180)
    btn_10_7=tkinter.Button(root_10,text="行列式",command=partial(get,5),width=30,font=("",15))
    btn_10_7.place(x=600,y=220)
    btn_10_8=tkinter.Button(root_10,text="階数",command=partial(get,6),width=30,font=("",15))
    btn_10_8.place(x=600,y=260)
    btn_10_9=tkinter.Button(root_10,text="トレース",command=partial(get,7),width=30,font=("",15))
    btn_10_9.place(x=600,y=300)
    btn_10_10=tkinter.Button(root_10,text="固有値",command=partial(get,8),width=30,font=("",15))
    btn_10_10.place(x=600,y=340)
    btn_10_11=tkinter.Button(root_10,text="対角化行列",command=partial(get,9),width=30,font=("",15))
    btn_10_11.place(x=600,y=380)
    btn_10_12=tkinter.Button(root_10,text="対角行列",command=partial(get,10),width=30,font=("",15))
    btn_10_12.place(x=600,y=420)

    lbl_10_1=tkinter.Label(root_10,text="A:",font=("",20))
    lbl_10_1.place(x=0,y=95)
    lbl_10_2=tkinter.Label(root_10,text="行",font=("",20))
    lbl_10_2.place(x=65,y=95)
    lbl_10_3=tkinter.Label(root_10,text="列",font=("",20))
    lbl_10_3.place(x=135,y=95)
    lbl_10_4=tkinter.Label(root_10,text="↓",font=("",38))
    lbl_10_4.place(x=380,y=220)
    lbl_10_5=tkinter.Label(root_10,text="A=",font=("",40))
    lbl_10_5.place(x=200,y=80)
    lbl_10_6=tkinter.Label(root_10,text="=",font=("",40))
    lbl_10_6.place(x=230,y=350)

    txt_10_1=tkinter.Text(root_10,width=20,height=7,font=("",20))
    txt_10_1.place(x=270,y=20)
    txt_10_2=tkinter.Text(root_10,width=20,height=7,font=("",20))
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

main_window()
