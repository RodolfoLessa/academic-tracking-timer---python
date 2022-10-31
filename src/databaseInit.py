import sqlite3


def initDataBase():
        # DATABASE
        databaseName = "academic-tracking-timer.db";
        # Create a database or connect to one
        conn = sqlite3.connect(databaseName)
        # Create cursor
        c = conn.cursor()

        # CREATE TABLE - ATIVIDADES
        c.execute('''
                CREATE TABLE IF NOT EXISTS activities
                ([activity_id] INTEGER PRIMARY KEY, [activity_descrpition] TEXT UNIQUE)
                ''')

        c.execute('''
                CREATE TABLE IF NOT EXISTS subjects
                ([subject_id] INTEGER PRIMARY KEY, [subject_descrpition] UNIQUE)
                ''')


        c.execute('''
                CREATE TABLE IF NOT EXISTS registers
                (
                [id] INTEGER PRIMARY KEY, 
                [activity_id] INTEGER,
                [subject_id] INTEGER,
                [period_time] TIMESTAMP,
                FOREIGN KEY (activity_id) REFERENCES activities(activity_id), 
                FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
                )
                ''')

        conn.commit()
        conn.close()