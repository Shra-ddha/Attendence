import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("Management")

connection = sqlite3.connect('management.db')

TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_ROLL = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_ROLL + " INTEGER);")

appLabel = tk.Label(root, text="Attendance Management System", fg="#06a099", width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))


class Student(object):
    studentName = ""
    rollNo = ""
  

    def __init__(self, studentName, rollNo=0):
        self.studentName = studentName
        self.__rollNo = rollNo


nameLabel = tk.Label(root, text="Enter your student name", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0),
                                                pady=(30, 0))
rollLabel = tk.Label(root, text="Enter roll number ", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))

nameEntry = tk.Entry(root, width = 30)
rollEntry = tk.Entry(root, width = 30)

nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
rollEntry.grid(row=2, column=1, padx=(0,10), pady = 20)

def takeNameInput():
    global nameEntry, rollEntry
    # global studentName, rollNo
    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_ROLL
    studentName = nameEntry.get()
    nameEntry.delete(0, tk.END)
    rollNo = rollEntry.get()
    rollEntry.delete(0, tk.END)
    if studentName== '' or rollNo == '':
            messagebox.showerror('Error','Please fill both studentName and rollNo')
    else:
        try:
            # rollNo = 'three' # value error
            # rollNo = '3'
            rollNo = int(rollNo)
        except ValueError:
            messagebox.showerror('title','only digits are allowed in rollNo gap')



    connection.execute("INSERT INTO " + TABLE_NAME + " ( "  + STUDENT_NAME + ", " + STUDENT_ROLL + ") VALUES ('"+ studentName + "', "+ str(rollNo) +");")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")


def destroyRootWindow():
    root.destroy()
    secondWindow = tk.Tk()

    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Attendance Management System",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="Roll No")
  

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()


# def printDetails():
#     for singleItem in list:
#         print("Student name is: %s\nCollege name is: %s\nPhone number is: %d\nAddress is: %s" %
#               (singleItem.studentName, singleItem.rollNo, singleItem.phoneNumber, singleItem.address))
#         print("****************************************")

button = tk.Button(root, text="Save", command=lambda :takeNameInput())
button.grid(row=5, column=0, pady=30)

displayButton = tk.Button(root, text="Display Attendance", command=lambda :destroyRootWindow())
displayButton.grid(row=5, column=1)

root.mainloop()