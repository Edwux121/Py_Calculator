import tkinter  as tk 
from tkinter import * 

import mysql.connector
from mysql.connector import Error

class Mysql_connect:
    """"Class for handeling mysql connection"""

    def __init__(self, entry_data="1+1", answer=1, frame="placeholder"):
        self.entry_data = entry_data
        self.answer = answer
        self.frame = frame
        self.connection = None

    def connect(self):
        """Connect to the MySQL"""
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database = "calculator",
            )

            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = self.connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
        

        except Error as e:
            print("Error while connecting to MySQL", e)

        #finally:
        #    if connection.is_connected():
        #        cursor.close()
        #        connection.close()
        #        print("MySQL connection is closed")

    def insert(self, entry_data, answer):
        """Insert data to the database"""

        try:
            cursor = self.connection.cursor(prepared=True)
            sql_insert_query = """INSERT INTO calculations (query, answer) VALUES (%s, %s)"""
            qurey_variables = (entry_data, answer)
            cursor.execute(sql_insert_query, qurey_variables)
            self.connection.commit()

        except Error as e:
            print("Could not insert data to the database", e)

    def show_data(self, frame):
        """"Prints data from the Database"""

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM calculations LIMIT 10")

            i = 0
            for entry in cursor:
                for j in range(len(entry)):
                    e = Entry(frame, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, entry[j])
                i = i + 1

        except Error as e:
            print("Unable to print daata from the database", e)