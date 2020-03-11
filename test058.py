import tkinter
import sys
import math
from sympy import *

#main window
def main_window():
    root_1=tkinter.Tk()
    root_1.title(u"math")
    root_1.geometry("600x230")
    root_1.resizable(False, False)
    #root_1.configure(bg='#000000')

    btn_1=tkinter.Button(text="微分",command=sub_window_1,width=20,height=3)
    btn_1.place(x=0,y=30)
    btn_2=tkinter.Button(text="積分",command=sub_window_2,width=20,height=3)
    btn_2.place(x=150,y=30)
    btn_3=tkinter.Button(text="因数分解",command=sub_window_3,width=20,height=3)
    btn_3.place(x=300,y=30)
    btn_4=tkinter.Button(text="方程式",command=sub_window_4,width=20,height=3)
    btn_4.place(x=450,y=30)
    btn_5=tkinter.Button(text="テーラー展開",command=sub_window_5,width=20,height=3)
    btn_5.place(x=0,y=90)
    btn_6=tkinter.Button(text="階乗",command=sub_window_6,width=20,height=3)
    btn_6.place(x=150,y=90)
    btn_7=tkinter.Button(text="連立方程式",command=sub_window_7,width=20,height=3)
    btn_7.place(x=300,y=90)
    btn_8=tkinter.Button(text="BMI",command=sub_window_8,width=20,height=3)
    btn_8.place(x=450,y=90)
    btn_9=tkinter.Button(text="極限",command=sub_window_9,width=20,height=3)
    btn_9.place(x=0,y=150)
    btn_10=tkinter.Button(text="",width=20,height=3)
    btn_10.place(x=150,y=150)
    btn_11=tkinter.Button(text="",width=20,height=3)
    btn_11.place(x=300,y=150)

    btn_a=tkinter.Button(text="mathを閉じる",command=root_1.destroy,width=20,height=3,bg="#ffa300")
    btn_a.place(x=450,y=150)

    root_1.mainloop()

#微分   test038.py
def sub_window_1():
    root_2=tkinter.Toplevel()
    root_2.title(u"微分")
    root_2.geometry("1500x300")
    root_2.resizable(False, False)

    def dx():
        x = Symbol('x')
        y = Symbol('y')
        g = txt_2_1.get()
        a = txt_2_3.get()

        if a=="x":
            f = diff(g,x)
        elif a=="y":
            f = diff(g,y)
        elif a=="xx":
            f = diff(g,x)
            f = diff(f,x)
        elif a=="xy":
            f = diff(g,x)
            f = diff(f,y)
        elif a=="yx":
            f = diff(g,y)
            f = diff(f,x)
        elif a=="yy":
            f = diff(g,y)
            f = diff(f,y)

        f=str(f)

        #txt_2_1.delete(0,tkinter.END)
        #txt_2_1.insert(0,g.replace("**","A").replace("*","").replace("A","^"))
        txt_2_2.delete(0,tkinter.END)
        txt_2_2.insert(0,f.replace("**","A").replace("*","").replace("A","^"))

    btn_2_1=tkinter.Button(root_2,text="計算",width=20,command=dx,font=10)
    btn_2_1.place(x=500,y=150)
    btn_2_2=tkinter.Button(root_2,text="微分を閉じる",width=20,command=root_2.destroy,font=10)
    btn_2_2.place(x=500,y=200)

    txt_2_1=tkinter.Entry(root_2,width=70,font=("",30))
    txt_2_1.place(x=70,y=50)
    txt_2_2=tkinter.Entry(root_2,width=70,font=("",30))
    txt_2_2.place(x=70,y=90)
    txt_2_3=tkinter.Entry(root_2,width=2,font=("",30))
    txt_2_3.place(x=1400,y=250)
    txt_2_3.insert(0,"x")

    lbl_2_1=tkinter.Label(root_2,text="関数",font=50)
    lbl_2_1.place(x=20,y=50)
    lbl_2_2=tkinter.Label(root_2,text="導関数",font=50)
    lbl_2_2.place(x=-5,y=90)

    root_2.mainloop()

#積分　　test046.py
def sub_window_2():
    root_10=tkinter.Toplevel()
    root_10.title(u"積分")
    root_10.geometry("1500x280")
    root_10.resizable(False, False)

    def integ():
        x = Symbol('x')

        f=txt_1.get()
        a=txt_2.get()
        b=txt_3.get()
        c=txt_5.get()
        c=int(c)

        g=integrate(f)
        A=g.subs(x,a)-g.subs(x,b)

        txt_4.delete(0,tkinter.END)
        lbl()

        if  c==0:
            txt_4.insert(0,A)

        elif c==1:
            txt_4.insert(0,A.evalf())

            if A!=A.evalf():
                lbl_2=tkinter.Label(text="dx≒",font=("",60))
                lbl_2.place(x=620,y=70)

        elif c==2:
            g=str(g)
            txt_4.insert(0,g.replace("**","A").replace("*","").replace("A","^"))


    txt_1=tkinter.Entry(root_10,width=20,font=("",40))
    txt_1.place(x=80,y=90)
    txt_2=tkinter.Entry(root_10,width=10)
    txt_2.place(x=30,y=50)
    txt_3=tkinter.Entry(root_10,width=10)
    txt_3.place(x=30,y=170)
    txt_4=tkinter.Entry(root_10,width=25,font=("",40))
    txt_4.place(x=800,y=90)
    txt_5=tkinter.Entry(root_10,width=1,font=("",30))
    txt_5.place(x=1400,y=10)
    txt_5.insert(0,0)

    def lbl():
         lbl_1=tkinter.Label(root_10,text="∫",font=("",70))
         lbl_1.place(x=-20,y=70)
         lbl_2=tkinter.Label(root_10,text="dx =",font=("",60))
         lbl_2.place(x=620,y=70)
         lbl_3=tkinter.Label(root_10,text="数値を出力するときは１を入力")
         lbl_3.place(x=1220,y=10)
         lbl_4=tkinter.Label(root_10,text="不定積分を出力するときは2を入力")
         lbl_4.place(x=1220,y=30)

    btn_1=tkinter.Button(root_10,text="計算",command=integ,width=30)
    btn_1.place(x=580,y=200)
    btn_2=tkinter.Button(root_10,text="積分を閉じる",command=root_10.destroy,width=30)
    btn_2.place(x=580,y=230)
    lbl()

    root_10.mainloop()

#因数分解　test064.py
def sub_window_3():
    root_4=tkinter.Toplevel()
    root_4.title(u"因数分解")
    root_4.geometry("1000x300")
    root_4.resizable(False, False)

    def fa():
        A=txt_4_1.get()
        B=factor(A)

        B=str(B)
        B=B.replace("**","C").replace("*","").replace("C","^")

        txt_4_2.delete(0,tkinter.END)
        txt_4_2.insert(0,B)

    btn_4_1=tkinter.Button(root_4,text="計算",command=fa,width=20,height=3)
    btn_4_1.place(x=400,y=110)
    btn_4_2=tkinter.Button(root_4,text="因数分解を閉じる",command=root_4.destroy,width=20)
    btn_4_2.place(x=400,y=250)

    txt_4_1=tkinter.Entry(root_4,width=40,font=("",30))
    txt_4_1.place(x=70,y=50)
    txt_4_2=tkinter.Entry(root_4,width=40,font=("",30))
    txt_4_2.place(x=70,y=180)

    lbl_4_1=tkinter.Label(root_4,text="因数分解したい式を入力してください",font=50)
    lbl_4_1.place(x=300,y=20)

    root_4.mainloop()

#方程式　　test044.py
def sub_window_4():
    root_9=tkinter.Toplevel()
    root_9.title(u"方程式")
    root_9.geometry("950x600")
    root_9.resizable(False, False)

    scrollbar_frame = tkinter.Frame(root_9)
    scrollbar_frame.grid(padx=100, pady=100)
    listbox2 = tkinter.Listbox(scrollbar_frame,height=15,width=70,font=40)

    def fx():
        x = Symbol('x')
        f=txt_9_1.get()
        A= solve(f, dict = True)

        listbox2.delete(0,tkinter.END)
        for i in range(0,len(A),1):
            listbox2.insert(tkinter.END,A[i])

    listbox2.pack(side=tkinter.LEFT)
    yscroll_bar =tkinter.Scrollbar(scrollbar_frame, command=listbox2.yview)
    yscroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    listbox2.config(yscrollcommand=yscroll_bar.set)

    btn_9_1=tkinter.Button(root_9,text="方程式を閉じる",command=root_9.destroy)
    btn_9_1.place(x=460,y=540)
    btn_9_2=tkinter.Button(root_9,text="計算",command=fx,font=40)
    btn_9_2.place(x=470,y=480)

    txt_9_1=tkinter.Entry(root_9,width=70,font=40)
    txt_9_1.place(x=100,y=50)

    lbl_9_1=tkinter.Label(root_9,text="方程式",font=40)
    lbl_9_1.place(x=0,y=50)
    lbl_9_2=tkinter.Label(root_9,text="解",font=40)
    lbl_9_2.place(x=20,y=170)
    lbl_9_3=tkinter.Label(root_9,text="=0",font=40)
    lbl_9_3.place(x=880,y=50)

    root_9.mainloop()

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
        root_7_2=tkinter.Tk()
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

#連立方程式　　test065.py
def sub_window_9():
    root_9=tkinter.Tk()
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

main_window()
