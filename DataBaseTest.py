from cProfile import label
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Tracker Academic Timer')
root.geometry("400x400")

# DATABASE
# Create a database or connect to one
conn = sqlite3.connect('student_data.db')
# Create cursor
c = conn.cursor()

# Create table
c.execute("""
        CREATE TABLE IF NOT EXISTS subject (
            course text,
            period integer
        )""")

# Create Function to Delete a Record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('student_data.db')
    # Create cursor
    c = conn.cursor()
    
    # Delete a record
    c.execute("DELETE from subject WHERE oid= " + delete_name.get())
    
    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

# Create Submit Function For database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('student_data.db')
    # Create cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute("INSERT INTO subject VALUES (:c_name, :p_name)",
              {
                  'c_name': c_name.get(),
                  'p_name': p_name.get()
              })

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear The Text Boxes
    c_name.delete(0, END)
    p_name.delete(0, END)

# Create Query Function For database
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('student_data.db')
    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM subject")
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
c_name = Entry(root, width=30)
c_name.grid(row=0, column=1, padx=20, pady=(10,0))
p_name = Entry(root, width=30)
p_name.grid(row=1, column=1)

delete_name = Entry(root, width=30)
delete_name.grid(row=4, column=1)

# Create Text Box Labels
c_name_label = Label(root, text="Course")
c_name_label.grid(row=0, column=0, padx=20, pady=(10,0))
p_name_label = Label(root, text="Time Period")
p_name_label.grid(row=1, column=0)

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
