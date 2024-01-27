from tkinter import *
from tkinter import messagebox

def play():
    for i in range(1, 10):
        button = Button(root, height=9, width=19, bd=9, relief='raised', bg='#d9b3ff', textvariable=buttons[i],
                        command=lambda i=i: press(i))
        button.grid(row=(i - 1) // 3 + 1, column=(i - 1) % 3, pady=10)

def press(num):
    global click, count
    sign = 'X' if click else 'O'
    buttons[num].set(sign)
    label = Label(root, text=sign, font="times 50 bold", bg='#d9b3ff', fg="maroon4")
    label.grid(row=(num - 1) // 3 + 1, column=(num - 1) % 3)
    
    count += 1
    click = not click
    checkWin()

def checkWin():
    global count

    for pattern in winning_patterns:
        if all(buttons[i].get() == 'X' for i in pattern):
            show_winner('X')
            return
        elif all(buttons[i].get() == 'O' for i in pattern):
            show_winner('O')
            return

    if count == 9:
        show_winner('Tie Game !')

def show_winner(winner):
    message = f"{winner} Wins !!" if winner in ('X', 'O') else "Tie Game !"
    messagebox.showinfo("Tic-Tac-Toe", message)
    reset()

def reset():
    for i in range(1, 10):
        buttons[i].set('')
    play()

root = Tk()
root.title('Tic-Tac-Toe')
root.geometry("620x630")
root.config(bg="lavender")

buttons = {i: StringVar() for i in range(1, 10)}
click = True
count = 0

title = Label(root, text="Tic Tac Toe Game", font="algerian 50 bold underline", fg="maroon4", bg='lavender')
title.grid(row=0, column=0, columnspan=3)

winning_patterns = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  
    [1, 4, 7], [2, 5, 8], [3, 6, 9], 
    [1, 5, 9], [3, 5, 7]  
]

play()
root.mainloop()
