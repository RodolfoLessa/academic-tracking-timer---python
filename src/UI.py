from cProfile import label
from tkinter import *
from webbrowser import get
from PIL import ImageTk, Image
#Import functions from CRUD
import CRUD

def query(root):
    subjects = CRUD.SelectAllSubjects()
    print_subjects = ''
    for subject in subjects:
        print_subjects += str(subject) + "\n"
    
    query_label = Label(root, text=print_subjects)
    query_label.grid(row=7, column=0, columnspan=2)

def initInterface():
    root = Tk()
    root.title('Tracker Academic Timer')
    root.geometry("1000x400")

    # Inserir Materia
    # Create Text Box
    subject_name = Entry(root, width=30)
    subject_name.grid(row=1, column=0, padx=20, pady=(10,0))

    # Create Text Box Labels
    subject_name_label = Label(root, text="Matéria")
    subject_name_label.grid(row=0, column=0, padx=20, pady=(10,0))

    # Create Submit Button
    submit_button_subject = Button(root, text="Adicionar Matéria", command = CRUD.insertSubject(subject_name.get()))
    submit_button_subject.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    subject_name.delete(0, END)

    # Create Query Button
    query_button = Button(root, text="Mostrar Matérias", command=query(root))
    query_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=132)

    root.mainloop()


