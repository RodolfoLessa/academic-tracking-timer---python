from atexit import register
from cProfile import label
from cgitb import text
from tkinter import *
import tkinter as tk
from tkinter import ttk
from webbrowser import get
from PIL import ImageTk, Image
import datetime
from datetime import datetime, timedelta
import time
import matplotlib.pyplot as plt

import databaseInit
import CRUD


databaseInit.initDataBase()

root = Tk()
root.title('Tracker Academic Timer')
root.geometry("1300x400")

def submit_subject():

    CRUD.insertSubject(subject_name.get())
    # Clear The Text Boxes
    subject_name.delete(0, END)

def delete_subject():
    subject = CRUD.SelectSubjectByDescription(delete_subject_name.get())
    CRUD.DeleteSubjectById(subject['id'])
    delete_subject_name.delete(0, END)

def query_subject():
    subjects = CRUD.SelectAllSubjects()
    print_subjects = ''
    for subject in subjects:
        print_subjects += str(subject) + "\n"
    
    query_label = Label(root, text=print_subjects)
    query_label.grid(row=7, column=0, columnspan=2)

def insert_activities():
    CRUD.insertActivity('Aula')
    CRUD.insertActivity('Exercícios')
    CRUD.insertActivity('Leitura')
    CRUD.insertActivity('Laboratório')
    CRUD.insertActivity('Trabalho Prático')
    
def query_activity():
    activities = CRUD.SelectAllActivities()
    print_activities = ''
    for activity in activities:
        print_activities += str(activity) + "\n"  
    
    query_label = Label(root, text=print_activities)
    query_label.grid(row=7, column=3, columnspan=2)

def insert_register():
    subject = CRUD.SelectSubjectByDescription(course_name.get())
    activity = CRUD.SelectActivityByDescription(activity_name.get())
    
    hourbegin = datetime.strptime(hourbegin_name.get(), "%d/%m/%Y %H:%M:%S")
    hourbegin = datetime.timestamp(hourbegin)

    hourend = datetime.strptime(hourend_name.get(), "%d/%m/%Y %H:%M:%S")
    hourend = datetime.timestamp(hourend)

    period = hourend - hourbegin

    CRUD.insertRegister(activity['activity_descrpition'], subject['subject_description'], period)
    # Clear The Text Boxes
    activity_name.delete(0, END)
    course_name.delete(0, END)
    hourbegin_name.delete(0, END)
    hourend_name.delete(0, END)
    
    e1_str.set(time_begin)
    e2_str.set(time_end)

def query_register():
    registers = CRUD.SelectAllRegisters()
    print_registers = ''
    for register in registers:
        print_registers += str(register) + "\n"  
    
    query_label = Label(root, text=print_registers)
    query_label.grid(row=7, column=6, columnspan=2)

def delete_register():
    CRUD.DeleteRegisterById(delete_register_name.get())
    delete_register_name.delete(0,END)

def convert_timestamp(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    dt_object = dt_object + timedelta(hours=-21) 
    epoch_time = datetime(1969, 12, 31)
    dt_object = dt_object - epoch_time
    minutes = dt_object.total_seconds()/60
    return minutes


def data_subject():
    regs = CRUD.SumSubjectsFromRegister()
    for reg in regs:
        reg['periodo'] = convert_timestamp(reg['periodo'])

    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    axes.bar(
        range(len(regs)),
        [reg['periodo'] for reg in regs],
        tick_label = [reg['materia'] for reg in regs]
    )
    plt.show()

# CAMPO DE MATERIA
# Create Text Box
subject_name = Entry(root, width=20)
subject_name.grid(row=0, column=1, padx=20, pady=(10,0))
delete_subject_name = Entry(root, width=20)
delete_subject_name.grid(row=3, column=1)
# Create Text Box Labels
subject_name_label = Label(root, text="Matéria")
subject_name_label.grid(row=0, column=0, padx=20, pady=(10,0))
delete_subject_name_label = Label(root, text="ID Delete")
delete_subject_name_label.grid(row=3, column=0)
# Create Submit Button
submit_button_subject = Button(root, text="Adicionar Matéria", command = submit_subject)
submit_button_subject.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=50)
# Create Query Button
query_button = Button(root, text="Mostrar Matérias", command=query_subject)
query_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=50)
# Create Delete Button
delete_subject_button = Button(root, text="Deletar Matéria", command=delete_subject)
delete_subject_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

# CAMPO DE ATIVIDADE
# Create Text Box Labels
activity_name_label = Label(root, text="Atividades")
activity_name_label.grid(row=0, column=3, padx=20, pady=(10,0))
# Create Query Button
query_button = Button(root, text="Mostrar Atividades", command=query_activity)
query_button.grid(row=1, column=3, columnspan=2, pady=10, padx=10, ipadx=50)

# CAMPO REGISTRO
# Create Text Box
time_begin = time.strftime("%d/%m/%Y %H:%M:%S")
e1_str = tk.StringVar()
e1_str.set(time_begin)

time_end = time.strftime("%d/%m/%Y %H:%M:%S")
e2_str = tk.StringVar()
e2_str.set(time_end)

hourbegin_name = Entry(root,textvariable=e1_str, width=20)
hourbegin_name.grid(row=1, column=6)
hourend_name = Entry(root,textvariable=e2_str, width=20)
hourend_name.grid(row=1, column=7)
course_name = Entry(root, width=20)
course_name.grid(row=1, column=8)
activity_name = Entry(root, width=20)
activity_name.grid(row=1, column=9)
delete_register_name = Entry(root, width=20)
delete_register_name.grid(row=3, column=6)

# Create Text Box Labels
hourbegin_name_label = Label(root, text="Início")
hourbegin_name_label.grid(row=0, column=6)
hourend_name_label = Label(root, text="Fim")
hourend_name_label.grid(row=0, column=7)
course_name_label = Label(root, text="Curso ID")
course_name_label.grid(row=0, column=8)
activity_name_label = Label(root, text="Atividade ID")
activity_name_label.grid(row=0, column=9)
delete_register_name_label = Label(root, text="ID Delete")
delete_register_name_label.grid(row=3, column=5)


# Create Registers Buttons
query_button_register = Button(root, text="Mostrar Registros", command=query_register)
query_button_register.grid(row=2, column=7, columnspan=2, pady=10, padx=10, ipadx=50)
register_button = Button(root, text="Inserir Registro", command=insert_register)
register_button.grid(row=2, column=5, columnspan=2, pady=10, padx=10, ipadx=50)
register_button_delete = Button(root, text="Deletar Registro", command=delete_register)
register_button_delete.grid(row=3, column=7, columnspan=2, pady=10, padx=10, ipadx=50)

# Botões de Visualização de Dados
data_button_subject = Button(root, text="Ver horas de Materia", command= data_subject)
data_button_subject.grid(row=5, column=7, columnspan=2, pady=10, padx=10, ipadx=30)



insert_activities()
root.mainloop()
    