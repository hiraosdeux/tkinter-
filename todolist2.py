from tkinter import * 
from tkinter import messagebox
from tkinter import simpledialog

c = Tk()
c.title('TO DO LIST')
c.config(bg="lightblue")
c.geometry('600x400')
#****************************************************************************
def nav(l1,l2):
    indexlist=l1.curselection()
    if indexlist :
        index=indexlist[0]
        val=l1.get(index)
        l1.delete(index)
        l2.insert(END,val)

def move(entry1,lb):
            text = entry1.get()
            if text:
                lb.insert(END, text)
                entry1.delete(0, END)
def delete():
    selected = lb.curselection()
    lb.delete(selected)
def clear():
    lb.delete(0, END)
    messagebox.showinfo('Info', 'Deleted')

#******************************************************************************
n1=Label(c,text="DO IT",fg="red",bg="lightblue",font=('Arial',14,"bold")).place(x=60,y=35)


frame = Frame(c)
frame.place(x=60,y=60)

lb = Listbox(frame,selectmode = "multiple")
lb.pack(side=LEFT)

sb = Scrollbar(frame, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)

lb.configure(yscrollcommand=sb.set)
sb.config(command=lb.yview)
lb.insert(0,"Eat apple")
lb.insert(1,"Go to gym")
lb.insert(2,"Learn something")

#**************************************************************
n1=Label(text="Already did",fg="green",bg="lightblue",font=('Arial',14,"bold")).place(x=430,y=35)
lo=Listbox(c,width=20,height=10,selectmode="multiple")
lo.place(x=430,y=60)
#******************************************************************
n1=Label(c,text="What do you want to do ? :",bg="lightblue",font=('Arial',14,"bold"))
n1.place(x=50,y=270)
entry1=Entry(c,width=50)
entry1.place(x=200,y=300)

#**************************************************************
btn1=Button(text="ADD",width=10,bg="green",fg='white',command=lambda : move(entry1,lb)).place(x=280,y=100)
btn2=Button(text="DELETE",width=10,bg="red",fg='white',command=delete).place(x=280,y=130)
btn3=Button(text="CLEAR",width=10,bg="blue",fg='white',command=clear).place(x=280,y=160)
#*************************************************************
btn4=Button(text="=>",width=5,command=lambda : nav(lb , lo)).place(x=340,y=200)
btn5=Button(text="<=",width=5,command=lambda : nav(lo , lb)).place(x=260,y=200)
c.mainloop()


