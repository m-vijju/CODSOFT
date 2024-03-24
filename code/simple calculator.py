from tkinter import*
strng=""
def click(n):
    global strng
    strng=strng+str(n)
    eq.set(strng)

def equalto():
    try:
        global strng
        result=str(eval(strng))
        eq.set(result)
        strng=""
    except:
        eq.set(" invalid ")
        strng=""
def clear():
    global strng
    strng=""
    eq.set("")

def into():
    global strng
    if strng:
       strng2=strng[:-1]
       exp_f.delete(0,END)
       exp_f.insert(0,strng2)
       strng=strng2

if __name__=="__main__":
    gui=Tk()
    gui.configure(bg="blue")
    gui.title("calculator")
    gui.geometry("270x150")
    eq=StringVar()

    exp_f=Entry(gui,textvariable=eq)
    exp_f.grid(columnspan=10,ipadx=80)
    button1=Button(gui,text=" 1 ",fg="blue",bg="white",command=lambda:click(1),height=1,width=7)
    button1.grid(row=2,column=0)
    button2=Button(gui,text=" 2 ",fg="blue",bg="white",command=lambda:click(2),height=1,width=7)
    button2.grid(row=2,column=1)
    button3=Button(gui,text=" 3 ",fg="blue",bg="white",command=lambda:click(3),height=1,width=7)
    button3.grid(row=2,column=2)
    button4=Button(gui,text=" 4 ",fg="blue",bg="white",command=lambda:click(4),height=1,width=7)
    button4.grid(row=3,column=0)
    button5=Button(gui,text=" 5 ",fg="blue",bg="white",command=lambda:click(5),height=1,width=7)
    button5.grid(row=3,column=1)
    button6=Button(gui,text=" 6 ",fg="blue",bg="white",command=lambda:click(6),height=1,width=7)
    button6.grid(row=3,column=2)
    button7=Button(gui,text=" 7 ",fg="blue",bg="white",command=lambda:click(7),height=1,width=7)
    button7.grid(row=4,column=0)
    button8=Button(gui,text=" 8 ",fg="blue",bg="white",command=lambda:click(8),height=1,width=7)
    button8.grid(row=4,column=1)
    button9=Button(gui,text=" 9 ",fg="blue",bg="white",command=lambda:click(9),height=1,width=7)
    button9.grid(row=4,column=2)
    button0=Button(gui,text=" 0 ",fg="blue",bg="white",command=lambda:click(0),height=1,width=7)
    button0.grid(row=5,column=1)
    plus=Button(gui,text=" + ",fg="blue",bg="white",command=lambda:click("+"),height=1,width=7)
    plus.grid(row=2,column=3)
    minus=Button(gui,text=" - ",fg="blue",bg="white",command=lambda:click("-"),height=1,width=7)
    minus.grid(row=3,column=3)
    multiply=Button(gui,text=" * ",fg="blue",bg="white",command=lambda:click("*"),height=1,width=7)
    multiply.grid(row=4,column=3)
    divide=Button(gui,text=" / ",fg="blue",bg="white",command=lambda:click("/"),height=1,width=7)
    divide.grid(row=5,column=3)
    equalto=Button(gui,text=" = ",fg="blue",bg="orange",command=equalto,height=1,width=7)
    equalto.grid(row=6,column=3)
    clear=Button(gui,text="Clear",fg="blue",bg="white",command=clear,height=1,width=7)
    clear.grid(row=6,column=1)
    decimal=Button(gui,text=" . ",fg="blue",bg="white",command=lambda:click("."),height=1,width=7)
    decimal.grid(row=5,column=2)
    into=Button(gui,text=" X ",fg="blue",bg="white",command=into,height=1,width=7)
    into.grid(row=5,column=0)
    gui.mainloop()
