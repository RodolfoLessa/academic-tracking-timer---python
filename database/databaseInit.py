import pandas as pd
import sqlite3

# DATABASE
databaseName = "academic-tracking-timer.db";
# Create a database or connect to one
conn = sqlite3.connect(databaseName)
# Create cursor
c = conn.cursor()

# CREATE TABLE - ATIVIDADES
c.execute('''
        CREATE TABLE IF NOT EXISTS activities
        ([activity_id] INTEGER PRIMARY KEY, [activity_descrpition] TEXT)
        ''')

c.execute('''
        CREATE TABLE IF NOT EXISTS subjects
        ([subject_id] INTEGER PRIMARY KEY, [subject_descrpition] TEXT)
        ''')


c.execute('''
        CREATE TABLE IF NOT EXISTS registers
        ([id] INTEGER PRIMARY KEY, 
        [activity_id] INTEGER,
        [subject_id] INTEGER,
        [start_date] DATE,
        [end_date] DATE,
        FOREIGN KEY (activity_id) REFERENCES activities (activity_id), 
        FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
        )
        ''')

conn.commit()
conn.close()