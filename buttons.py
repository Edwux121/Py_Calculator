import tkinter as tk
from tkinter import messagebox
from mysql_conn.mysql_connect import Mysql_connect

class Buttons:
    """Class for the calculator number buttons"""

    def __init__(self, myapp, txt_frame):
        self.myapp = myapp
        self.txt_frame = txt_frame
        self.last_operator = ""
        self.last_index = 0

        
        
    def define_buttons(self):
        self.validate = self.myapp.register(self.validation)
        self.entry = tk.Entry(self.txt_frame, width=30, font=('Arial 24'), validate="key", validatecommand=(self.validate, "%P"))

        self.button_9 = tk.Button(self.myapp, text="9", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("9"))
        self.button_8 = tk.Button(self.myapp, text="8", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("8"))
        self.button_7 = tk.Button(self.myapp, text="7", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("7"))
        self.button_6 = tk.Button(self.myapp, text="6", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("6"))
        self.button_5 = tk.Button(self.myapp, text="5", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("5"))
        self.button_4 = tk.Button(self.myapp, text="4", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("4"))
        self.button_3 = tk.Button(self.myapp, text="3", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("3"))
        self.button_2 = tk.Button(self.myapp, text="2", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("2"))
        self.button_1 = tk.Button(self.myapp, text="1", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("1"))
        self.button_0 = tk.Button(self.myapp, text="0", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("0"))
        self.button_plus = tk.Button(self.myapp, text="+", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("+"))
        self.button_minus = tk.Button(self.myapp, text="-", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("-"))
        self.button_multiply = tk.Button(self.myapp, text="*", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("*"))
        self.button_division = tk.Button(self.myapp, text="/", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("/"))
        self.button_enter = tk.Button(self.myapp, text="ENT", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("ENT"))
        self.button_delete = tk.Button(self.myapp, text="DEL", font=("Arial 24"), width=5, height=2, command=lambda:self.button_pressed("DEL"))

        #Putting each button into the grid
        self.entry.grid(column=0, row=3)
        self.button_plus.grid(column=3, row=1, padx=5, pady=5)
        self.button_9.grid(column=2, row=1, padx=5, pady=5)
        self.button_8.grid(column=1, row=1, padx=5, pady=5)
        self.button_7.grid(column=0, row=1, padx=5, pady=5)
        self.button_minus.grid(column=3, row=2, padx=5, pady=5)
        self.button_6.grid(column=2, row=2, padx=5, pady=5)
        self.button_5.grid(column=1, row=2, padx=5, pady=5)
        self.button_4.grid(column=0, row=2, padx=5, pady=5)
        self.button_multiply.grid(column=3, row=3, padx=5, pady=5)
        self.button_3.grid(column=2, row=3, padx=5, pady=5)
        self.button_2.grid(column=1, row=3, padx=5, pady=5)
        self.button_1.grid(column=0, row=3, padx=5, pady=5)
        self.button_division.grid(column=3, row=4, padx=5, pady=5)
        self.button_0.grid(column=2, row=4, padx=5, pady=5)
        self.button_enter.grid(column=0, row=4, padx=5, pady=5)
        self.button_delete.grid(column=1, row=4, padx=5, pady=5)

    def button_pressed(self, text):
        """Create empty string, which gets updated everytime a button is pressed and is shown to the user"""
        entry_value = self.entry.get()
        if entry_value:
            self.last_operator = entry_value[-1]
        if self.entry.get() and text == "DEL":
            #If entry is not empty delete last digit
            last_index = len(self.entry.get()) - 1
            self.entry.delete(last_index, tk.END)
        elif text == "ENT":
            #If ENT button is pressed convert whole entry to list and perform calculations
            value = self.entry.get()
            result = eval(value)
            #Mysql connection
            self.mysql_conn = Mysql_connect(value, result)
            self.mysql_conn.connect()
            try:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, float(result))

                #Adding the data to MySQL
                self.mysql_conn.insert(value, float(result))

            except(SyntaxError, ZeroDivisionError, TypeError):
                messagebox.showerror("Wrong syntax", "Wrong syntax error!")
        elif text == "*" or text == "/" or text == "-" or text == "+" or text == ".":
            #Check if the symbol was used twice in a row
            last_index = len(self.entry.get()) - 1
            if self.last_operator == "*" or self.last_operator == "/" or self.last_operator == "-" or self.last_operator == "+" or self.last_operator == ".":
                #if duplicate, delete the original symbol
                self.entry.delete(last_index, tk.END)
            self.entry.insert(tk.END, text)
        else:
            #Insert new number or symbol
            self.entry.insert(tk.END, text)
            

    def validation(self, new_value):
        """Entry validation"""
        allowed_nums = "0123456789"
        allowed_chars = "/*-+."
        last_index = len(self.entry.get()) - 1 #Used to check last index in order to avoid using symbols as a first value
        if new_value == "":
            return True
        elif any(i in allowed_nums for i in new_value) and len(new_value) <= 20:
            return True
        elif any(i in allowed_chars for i in new_value):
            if last_index < 0:
                return False
            else:
                return True
        else:
            return False