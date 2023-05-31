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
        new_window.minsize(600, 600)

        db_frame = tk.Frame(new_window, width=300, height=500)
        db_frame.grid(column=0, row=0)

        #Print data from the database
        data = Mysql_connect(new_window)
        data.connect()
        data.show_data(new_window)