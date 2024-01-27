from tkinter import *
import math


class Calculate:
    def __init__(self, window):
        self.root = window
        window.geometry("295x280")
        window.title("Rihab mahdi")
        self.en1 = Entry(window, font=("cursive", 15, "bold"))
        self.en1.place(x=35, y=20)
        self.btn1 = Button(window, text="1", font=("cursive", 15, "bold"), bg="silver", fg="white", borderwidth=2, relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation(1))
        self.btn1.place(x=10, y=60)
        self.btn2 = Button(window, text="2", font=("cursive", 15, "bold"), bg="silver", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation(2))
        self.btn2.place(x=65, y=60)
        self.btn3 = Button(window, text="3", font=("cursive", 15, "bold"), bg="silver", fg="white", borderwidth=2, relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation(3))
        self.btn3.place(x=120, y=60)
        self.btn4 = Button(window, text="DEL", font=("cursive", 15, "bold"), bg="#48D1CC", fg="white", borderwidth=2, relief="ridge", cursor="dot", width=4, command=self.del_last_char)
        self.btn4.place(x=175, y=60)
        self.btn5 = Button(window, text="AC", font=("cursive", 15, "bold"), bg="#48D1CC", fg="white", borderwidth=2, relief="ridge", cursor="dot", width=4, command=self.clear_field)
        self.btn5.place(x=225, y=60)
        self.btn6 = Button(window, text="4", font=("cursive", 15, "bold"), bg="silver", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation(4))
        self.btn6.place(x=10, y=101)
        self.btn7 = Button(window, text="5", font=("cursive", 15, "bold"), bg="silver", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation(5))
        self.btn7.place(x=65, y=101)
        self.btn8 = Button(window, text="6", font=("cursive", 15, "bold"), bg="silver", fg="white", borderwidth=2, relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation(6))
        self.btn8.place(x=120, y=101)
        self.btn9 = Button(window, text="*", font=("cursive", 15, "bold"), bg="#48D1CC", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation("*"))
        self.btn9.place(x=175, y=101)
        self.btn10 = Button(window, text="/", font=("cursive", 15, "bold"), bg="#48D1CC", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation("/"))
        self.btn10.place(x=225, y=101)
        self.btn11 = Button(window, text="7", font=("cursive", 15, "bold"), bg="silver", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation(7))
        self.btn11.place(x=10, y=141)
        self.btn12 = Button(window, text="8", font=("cursive", 15, "bold"), bg="silver", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation(8))
        self.btn12.place(x=65, y=141)
        self.btn13 = Button(window, text="9", font=("cursive", 15, "bold"), bg="silver", fg="white", borderwidth=2, relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation(9))
        self.btn13.place(x=120, y=141)
        self.btn14 = Button(window, text="+", font=("cursive", 15, "bold"), bg="#48D1CC", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation("+"))
        self.btn14.place(x=175, y=141)
        self.btn15 = Button(window, text="-", font=("cursive", 15, "bold"), bg="#48D1CC", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation("-"))
        self.btn15.place(x=225, y=141)
        self.btn16 = Button(window, text="log10", font=("cursive", 15, "bold"), bg="#48D1CC", fg="white", borderwidth=2, relief="ridge", cursor="dot", width=4, command=self.log10)
        self.btn16.place(x=10, y=181)
        self.btn17 = Button(window, text="0", font=("cursive", 15, "bold"), bg="silver", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation(0))
        self.btn17.place(x=65, y=181)
        self.btn18 = Button(window, text="MOD", font=("cursive", 15, "bold"), bg="#48D1CC", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation("%"))
        self.btn18.place(x=120, y=181)
        self.btn19 = Button(window, text="=", font=("cursive", 15, "bold"), bg="#20B2AA", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=22, command=self.evaluate_calculation)
        self.btn19.place(x=10, y=221)
        self.btn20 = Button(window, text="√", font=("cursive", 15, "bold"), bg="#48D1CC", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=4, command=self.sqrt)
        self.btn20.place(x=175, y=181)
        self.btn21 = Button(window, text="^", font=("cursive", 15, "bold"), bg="#48D1CC", fg="white", borderwidth=2,relief="ridge", cursor="dot", width=4, command=lambda: self.add_to_calculation("**"))
        self.btn21.place(x=225, y=181)


        
        self.calculation = ""
    #*************les fonctions***********************************************
    def add_to_calculation(self, symbol):
        self.calculation += str(symbol)
        self.en1.delete(0, END)
        self.en1.insert(0, self.calculation)

    def clear_field(self):
        self.calculation = ""
        self.en1.delete(0, END)

    def del_last_char(self):
        self.calculation = self.calculation[:-1]
        self.en1.delete(0, END)
        self.en1.insert(0, self.calculation)

    def evaluate_calculation(self):
        try:
            self.calculation = str(eval(self.calculation))
            self.en1.delete(0, END)
            self.en1.insert(0, self.calculation)
        except:
            self.clear_field()
            self.en1.insert(0, "Error")
    def log10(self):
        try:
            result = math.log10(float(self.calculation))
            self.calculation = str(result)
            self.en1.delete(0, END)
            self.en1.insert(0, self.calculation)
        except ValueError:
            self.clear_field()
            self.en1.insert(0, "Error")
    def sqrt(self):
        try:
            result = math.sqrt(float(self.calculation))
            self.calculation = str(result)
            self.en1.delete(0, END)
            self.en1.insert(0, self.calculation)
        except ValueError:
            self.clear_field()
            self.en1.insert(0, "Error")


root = Tk()
app = Calculate(root)
root.mainloop()
