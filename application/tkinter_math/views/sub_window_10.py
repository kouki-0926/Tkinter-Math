import tkinter
from functools import partial
from sympy import *
from tkinter_math.calculation import *

def sub_window_10():
    def calc_10(type):
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

            anser=matrix.calculation(A,Ar,Ac,type)

            txt_10_5.delete(0,tkinter.END)
            txt_10_5.insert(0,anser[3])
            txt_10_2.delete("0.end",tkinter.END)
            if anser[4]=="MATRIX":
                for k in range(0,anser[1],1):
                    B=str(anser[0].row(k))
                    B=B.replace("Matrix","").replace("**","^").replace("*","").replace("([[","[").replace("]])","]\n")
                    txt_10_2.insert(f"{k+1}.{0}",B)
            elif anser[4]=="NUMBER":
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
    btn_10_2=tkinter.Button(root_10,text="A",command=partial(calc_10,"A"),width=30,font=("",15))
    btn_10_2.place(x=1030,y=20)
    btn_10_3=tkinter.Button(root_10,text="n乗",command=partial(calc_10,"A^n"),width=30,font=("",15))
    btn_10_3.place(x=1030,y=60)
    btn_10_4=tkinter.Button(root_10,text="転置",command=partial(calc_10,"A^t"),width=30,font=("",15))
    btn_10_4.place(x=1030,y=100)
    btn_10_5=tkinter.Button(root_10,text="逆行列",command=partial(calc_10,"A^-1"),width=30,font=("",15))
    btn_10_5.place(x=1030,y=140)
    btn_10_6=tkinter.Button(root_10,text="余因子行列",command=partial(calc_10,"A~"),width=30,font=("",15))
    btn_10_6.place(x=1030,y=180)
    btn_10_7=tkinter.Button(root_10,text="行列式",command=partial(calc_10,"det(A)"),width=30,font=("",15))
    btn_10_7.place(x=1030,y=220)
    btn_10_8=tkinter.Button(root_10,text="階数",command=partial(calc_10,"rank(A)"),width=30,font=("",15))
    btn_10_8.place(x=1030,y=260)
    btn_10_9=tkinter.Button(root_10,text="トレース",command=partial(calc_10,"tr(A)"),width=30,font=("",15))
    btn_10_9.place(x=1030,y=300)
    btn_10_10=tkinter.Button(root_10,text="固有値",command=partial(calc_10,"λ"),width=30,font=("",15))
    btn_10_10.place(x=1030,y=340)
    btn_10_11=tkinter.Button(root_10,text="対角化行列",command=partial(calc_10,"P"),width=30,font=("",15))
    btn_10_11.place(x=1030,y=380)
    btn_10_12=tkinter.Button(root_10,text="対角行列",command=partial(calc_10,"P^-1AP"),width=30,font=("",15))
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
