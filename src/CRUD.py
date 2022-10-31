import sqlite3

#Region CREATE

def insertSubject(subject):
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()
    
    queryInsert = "INSERT OR IGNORE INTO subjects (subject_descrpition) VALUES ('" + subject +"')"
    c.execute(queryInsert)

    conn.commit()
    c.close()

def insertActivity(activity):
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()
    
    queryInsert = "INSERT OR IGNORE INTO activities (activity_descrpition) VALUES ('" + activity +"')"
    c.execute(queryInsert)
    
    conn.commit()
    c.close()

def insertRegister(activity_id, subject_id, period_time):
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()    
    
    insertQuery = """ INSERT INTO registers (activity_id, subject_id, period_time) VALUES (?, ?, ?)"""   
    c.execute(insertQuery, (str(activity_id), str(subject_id), period_time))
    
    conn.commit()
    c.close()

#Region DELETE
def DeleteRegisterById(id):
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()
    
    deleteQuery = "DELETE FROM registers WHERE id = "+ str(id)
    c.execute(deleteQuery)
    
    conn.commit()
    c.close()

def DeleteSubjectById(id):
        # DATABASE
    databaseName = "academic-tracking-timer.db"
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()
    
    deleteQuery = "DELETE FROM subjects WHERE subject_id = "+ str(id)
    c.execute(deleteQuery)
    
    conn.commit()
    c.close()

def DeleteActivityById(id):
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()
    
    deleteQuery = "DELETE FROM activities WHERE activity_id = "+ str(id)
    c.execute(deleteQuery)
    
    conn.commit()
    c.close()

#Region READ

def SelectSubjectByDescription(description):
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()
    
    querySelect = "SELECT * FROM subjects WHERE subject_descrpition = '"+ description + "'"
    c.execute(querySelect)
    
    ret = c.fetchall()
    subject = {
        'id': ret[0][0], 
        'subject_description': ret[0][1]
        }
    conn.commit()
    c.close()
    
    return subject

def SelectSubjectById(id):
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()
        
    querySelect = "SELECT * FROM subjects WHERE subject_id = "+ str(id)
    c.execute(querySelect)
    conn.commit()
    c.close()
    return 

def SelectAllSubjects():
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()    
    
    c.execute("SELECT * FROM subjects")
    subjects = c.fetchall()
    conn.commit()
    c.close()
    return subjects


def SelectActivityByDescription(description):
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()    
    
    querySelect = "SELECT * FROM activities WHERE activity_descrpition = '" + description + "'"
    c.execute(querySelect)
    ret = c.fetchall()
    activity = {
        'id': ret[0][0], 
        'activity_descrpition': ret[0][1]
        }

    conn.commit()
    c.close()
    return activity

def SelectActivityById(id):
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()
    
    querySelect = "SELECT * FROM activities WHERE activity_id = "+ str(id)

    c.execute(querySelect)
    conn.commit()
    c.close()

def SelectAllActivities():
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()
    
    c.execute("SELECT * FROM activities")
    activities = c.fetchall()
    
    conn.commit()
    c.close()
    return activities

def SelectRegisterByActivity(activity_id):
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()
    
    querySelect =  "SELECT * FROM registers WHERE activity_id = " + activity_id
    c.execute(querySelect)
    
    conn.commit()
    c.close()

def SelectRegisterBySubject(subject_id):
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()
    
    querySelect =  "SELECT * FROM registers WHERE subject_id = " + subject_id
    c.execute(querySelect)
    
    conn.commit()
    c.close()

def SelectAllRegisters():
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()

    c.execute("SELECT * FROM registers")
    registers = c.fetchall()
    conn.commit()
    c.close()
    return registers

def SumSubjectsFromRegister():
    # DATABASE
    databaseName = "academic-tracking-timer.db";
    # Create a database or connect to one
    conn = sqlite3.connect(databaseName)
    # Create cursor
    c = conn.cursor()
    querySelect = "SELECT subject_id,SUM(period_time) FROM registers GROUP BY subject_id;"
    sumSubjects = c.execute(querySelect).fetchall()    
    
    subjectsList = []
    for item in sumSubjects:
        subject = {
            'materia' : item[0],
            'periodo' : item[1]
        }
        print(item)
        print(subject)
        subjectsList.append(subject)

    conn.commit()
    c.close()
    return subjectsList