import datetime
import pandas as pd
import sqlite3

# DATABASE
databaseName = "academic-tracking-timer.db";
# Create a database or connect to one
conn = sqlite3.connect(databaseName)
# Create cursor
c = conn.cursor()

#Region CREATE
def insertSubject(C, conn, subject):
    queryInsert = "INSERT INTO subjects (subject_descrpition) VALUES ('" + subject +"')"
    C.execute(queryInsert)
    conn.commit()

def insertActivity(C, conn, activity):
    queryInsert = "INSERT INTO activities (activity_descrpition) VALUES ('" + activity +"')"
    C.execute(queryInsert)
    conn.commit()

def insertRegister(C, conn, activity_id, subject_id, start_date, end_date):
    insertQuery = """ INSERT INTO registers (activity_id, subject_id, start_date, end_date) VALUES (?, ?, ?, ?)"""   
    C.execute(insertQuery, (str(activity_id), str(subject_id), start_date, end_date))
    conn.commit()

#Region DELETE
def DeleteRegisterById(C, conn, id):
    deleteQuery = "DELETE FROM registers WHERE id = "+ str(id)
    C.execute(deleteQuery)
    conn.commit()

def DeleteSubjectById(C, conn, id):
    deleteQuery = "DELETE FROM subjects WHERE subject_id = "+ str(id)
    C.execute(deleteQuery)
    conn.commit()

def DeleteActivityById(C, conn, id):
    deleteQuery = "DELETE FROM activities WHERE activity_id = "+ str(id)
    C.execute(deleteQuery)
    conn.commit()

#Region READ

def SelectSubjectByDescription(C, conn, description):
    querySelect = "SELECT * FROM subjects WHERE subject_description = "+ description
    C.execute(querySelect)
    conn.commit()

def SelectSubjectById(C, conn, id):
    querySelect = "SELECT * FROM subjects WHERE subject_id = "+ str(id)
    C.execute(querySelect)
    conn.commit()

def SelectAllSubjects(C, conn):
    C.execute("SELECT * FROM subjects")
    conn.commit()

def SelectActivityByDescription(C, conn, description):
    querySelect = "SELECT * FROM activities WHERE activity_descrpition = "+ description
    C.execute(querySelect)
    conn.commit()

def SelectActivityById(C, conn, id):
    querySelect = "SELECT * FROM activities WHERE activity_id = "+ str(id)
    C.execute(querySelect)
    conn.commit()

def SelectAllActivities(C, conn):
    C.execute("SELECT * FROM activities")
    conn.commit()

def SelectRegisterByActivity(C, conn, activity_id):
    querySelect =  "SELECT * FROM registers WHERE activity_id = " + activity_id
    C.execute(querySelect)
    conn.commit()

def SelectRegisterBySubject(C, conn, subject_id):
    querySelect =  "SELECT * FROM registers WHERE subject_id = " + subject_id
    C.execute(querySelect)
    conn.commit()

def SelectAllRegisters(C, conn):
    C.execute("SELECT * FROM registers")
    conn.commit()

c.close()
