import tkinter
from functools import partial
from sympy import *
from tkinter_math.calculation import *

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
                B=B.replace("Matrix","").replace("**","^").replace("*","").replace("([[","[").replace("]])","]\n")
                txt_11_3.insert(f"{k+1}.{0}",B)
        except:
            txt_11_3.delete("0.end",tkinter.END)
            txt_11_3.insert("0.0","Error")


    root_11=tkinter.Toplevel()
    root_11.title(u"行列2")
    root_11.geometry("1400x500")
    root_11.resizable(False, False)

    btn_11_1=tkinter.Button(root_11,text="行列2を閉じる",width=30,command=root_11.destroy,font=("",15),bg="#ffa300")
    btn_11_1.place(x=1030,y=460)
    btn_11_2=tkinter.Button(root_11,text="A",command=partial(calc_11,"A"),width=30,font=("",15))
    btn_11_2.place(x=1030,y=260)
    btn_11_3=tkinter.Button(root_11,text="B",command=partial(calc_11,"B"),width=30,font=("",15))
    btn_11_3.place(x=1030,y=300)
    btn_11_4=tkinter.Button(root_11,text="kA+lB",command=partial(calc_11,"kA+lB"),width=30,font=("",15))
    btn_11_4.place(x=1030,y=340)
    btn_11_5=tkinter.Button(root_11,text="AB",command=partial(calc_11,"AB"),width=30,font=("",15))
    btn_11_5.place(x=1030,y=380)
    btn_11_6=tkinter.Button(root_11,text="BA",command=partial(calc_11,"BA"),width=30,font=("",15))
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
