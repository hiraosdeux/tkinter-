from tkinter import * 
from tkinter import messagebox

c = Tk()
c.title('TO DO LIST')
c.config(bg="beige")
c.geometry('400x400')
#****************************************************************************
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
def save():
    text = lb.get(0, END)
    with open('todolist.txt', 'w') as f:
        for i in text:
            f.write(str(i) + '\n')
    messagebox.showinfo('Info', 'Saved')
#******************************************************************************

frame = Frame(c)
frame.place(x=50,y=30)

lb = Listbox(frame,selectmode = "multiple",width=50)
lb.pack(side=LEFT)

sb = Scrollbar(frame, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)

lb.configure(yscrollcommand=sb.set)
sb.config(command=lb.yview)
lb.insert(0,"Eat apple")
lb.insert(1,"Go to gym")
lb.insert(2,"Learn something")

entry1=Entry(c,width=40)
entry1.place(x=80,y=220)

#**************************************************************
btn4=Button(text="SAVE",width=10,bg="white",fg='black',command=save).place(x=10,y=250)
btn1=Button(text="ADD",width=10,bg="green",fg='white',command=lambda : move(entry1,lb)).place(x=100,y=250)
btn2=Button(text="DELETE",width=10,bg="red",fg='white',command=delete).place(x=200,y=250)
btn3=Button(text="CLEAR",width=10,bg="blue",fg='white',command=clear).place(x=300,y=250)

c.mainloop()


