from cProfile import label
from tkinter import *
from webbrowser import get
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Tracker Academic Timer')
root.geometry("1000x400")

# DATABASE
# Create a database or connect to one
conn = sqlite3.connect('student_data_v1.db')
# Create cursor
c = conn.cursor()

# Create table
c.execute("""
        CREATE TABLE IF NOT EXISTS student_information (
            data integer,
            hour_begin integer,
            hour_end integer,
            course text,
            activity text
        )""")

# Create Function to Delete a Record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('student_data_v1.db')
    # Create cursor
    c = conn.cursor()
    
    # Delete a record
    c.execute("DELETE from student_information WHERE oid= " + delete_name.get())
    
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

# Create Submit Function For database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('student_data_v1.db')
    # Create cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute("INSERT INTO student_information VALUES (:date_name, :hourbegin_name, :hourend_name, :course_name, :activity_name)",
              {
                  'date_name': date_name.get(),
                  'hourbegin_name': hourbegin_name.get(),
                  'hourend_name': hourend_name.get(),
                  'course_name': course_name.get(),
                  'activity_name': activity_name.get()

              })

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear The Text Boxes
    date_name.delete(0, END)
    hourbegin_name.delete(0, END)
    hourend_name.delete(0, END)
    course_name.delete(0, END)
    activity_name.delete(0, END)

# Create Query Function For database
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('student_data_v1.db')
    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM student_information")
    records = c.fetchall()

    # Loop Thru Results
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=7, column=0, columnspan=2)

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


# INTERFACE
# Create Text Box
date_name = Entry(root, width=30)
date_name.grid(row=1, column=0, padx=20, pady=(10,0))

hourbegin_name = Entry(root, width=30)
hourbegin_name.grid(row=1, column=1)

hourend_name = Entry(root, width=30)
hourend_name.grid(row=1, column=2)

course_name = Entry(root, width=30)
course_name.grid(row=1, column=3)

activity_name = Entry(root, width=30)
activity_name.grid(row=1, column=4)


delete_name = Entry(root, width=30)
delete_name.grid(row=4, column=1)

# Create Text Box Labels
date_name_label = Label(root, text="Date")
date_name_label.grid(row=0, column=0, padx=20, pady=(10,0))

hourbegin_name_label = Label(root, text="Hour Begin")
hourbegin_name_label.grid(row=0, column=1)

hourend_name_label = Label(root, text="Hour End")
hourend_name_label.grid(row=0, column=2)

course_name_label = Label(root, text="Course")
course_name_label.grid(row=0, column=3)

activity_name_label = Label(root, text="Activity")
activity_name_label.grid(row=0, column=4)


delete_name_label = Label(root, text="ID Delete")
delete_name_label.grid(row=4, column=0)

# Create Submit Button
submit_button = Button(root, text="Add Time Tracker Databank", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create Query Button
query_button = Button(root, text="Show Databank", command=query)
query_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=132)

# Create Delete Button
delete_button = Button(root, text="Delete Record", command=delete)
delete_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=134)

# Commit Changes
conn.commit()
# Close Connection
conn.close()

root.mainloop()
