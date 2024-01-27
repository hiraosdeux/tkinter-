import tkinter as tk
from tkinter import messagebox, simpledialog
import ttkbootstrap as tkk
#********************************************************************
tasks = []

def add():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def update():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        updated_task = simpledialog.askstring("Update Task", "Enter the updated task:")
        if updated_task:
            tasks[selected_task_index[0]] = updated_task
            refresh()
        else:
            messagebox.showwarning("Warning", "Please enter a valid task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

def delete():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        del tasks[selected_task_index[0]]
        refresh()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def refresh():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)
#********************************************************************
c = tk.Tk()
c.title("To-Do List")
c.geometry("600x400")

#********************************************************************
n1=tk.Label(c,text="To do list",fg="green",font=('Arial',18,"bold"))
n1.pack(pady=5)
task_entry = tk.Entry(c, width=30)
task_entry.pack(pady=10)
task_listbox = tk.Listbox(c, selectmode=tk.SINGLE, height=10, width=40)
task_listbox.pack(pady=10)
#********************************************************************
add_button = tk.Button(c, text="Add Task",width=10,bg="green",fg='white', command=add)
add_button.pack(pady=5)
update_button = tk.Button(c, text="Update Task",width=10,bg="blue",fg='white', command=update)
update_button.pack(pady=5)
delete_button = tk.Button(c, text="Delete Task",width=10,bg="red",fg='white', command=delete)
delete_button.pack(pady=5)

c.mainloop()
