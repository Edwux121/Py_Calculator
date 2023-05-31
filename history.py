import tkinter as tk

from mysql_conn.mysql_connect import Mysql_connect

class History:
    """Class for History Window"""

    def __init__(self, root):
        self.root = root

    def open_new_window(self, root):
        """Opens History Window"""
        new_window = tk.Toplevel(root)
        new_window.title("History")
        new_window.minsize(400, 600)

        db_frame = tk.Frame(new_window, width=600, height=600)
        db_frame.grid(column=0, row=0)

        #Print data from the database
        data = Mysql_connect(db_frame)
        data.connect()
        data.show_data(db_frame)

        #Defining Labels for data
        id = tk.Label(db_frame, text="ID", borderwidth=1, relief="ridge", width=17, background="white")
        datatime = tk.Label(db_frame, text="Data", borderwidth=2, relief="ridge", width=17, background="white")
        query = tk.Label(db_frame, text="Calculation", borderwidth=2, relief="ridge", width=17, background="white")
        answer = tk.Label(db_frame, text="Solution", borderwidth=2, relief="ridge", width=17, background="white")
        id.grid(column = 0, row = 0)
        datatime.grid(column = 1, row = 0)
        query.grid(column = 2, row = 0)
        answer.grid(column = 3, row = 0)