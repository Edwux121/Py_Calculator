import tkinter as tk

from buttons import Buttons
from history import History

class Main:
    """"Main class for the app"""
    def __init__(self):
        self.myapp = App()
        self.myapp.master.title("Calculator")
        self.myapp.master.minsize(600, 600)

        #Creating a frame for buttons
        self.numbers_frame = tk.Frame(self.myapp, width=300, height=400)
        self.numbers_frame.grid(column=0, row=1)
        #Defining frame for text/output and filling it in
        self.text_frame = tk.Frame(self.myapp, width=300, height=200)
        self.text_frame.grid(column=0, row=0)

        #Defining History button fram and History class
        self.history_button_frame = tk.Frame(self.myapp, width=300, height=50)
        self.history_button_frame.grid(column=0, row=2)
        self.history = History(self.history_button_frame)
        
        #Defining the buttons.py
        self.buttons = Buttons(self.numbers_frame, self.text_frame)

        self.run_app()
        
        self.cloese_app()

    def run_app(self):
        """Function which provides text ant the buttons for the application"""
        #Calling the define_buttons function
        self.buttons.define_buttons()
        tk.Label(self.text_frame, text="").grid(column=0, row=1)
        tk.Label(self.text_frame, text="Calculator!", font = 'Arial 20 bold').grid(column=0, row=2)
        tk.Label(self.text_frame, text="").grid(column=0, row=4)

        #History button
        tk.Button(self.history_button_frame, text="History", font=("Arial 24"), width=23, height=2,
                   command=lambda:self.history.open_new_window(self.myapp)).grid(column=0, row=0)

    def cloese_app(self):
        self.myapp.mainloop()


class App(tk.Frame):
    """Class for manipulating the screen size"""
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

if __name__ == '__main__':
    #Run Main instance.
    ai = Main()