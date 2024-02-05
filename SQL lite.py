# don't need to install external applications
import sqlite3

# create database by connecting to database
# assign sqlite3 connection to variable db meaning database. And then ('name of table')
# this one is creates the database file.
db = sqlite3.connect('student_details')

# create cursor - allows me to execute sql statements inside of python and executes for us
cursor = db.cursor()
# single-user centralised database

# print statement to make sure everything is working.
print('Database connection established!')

# commits the connect command... Similar logic to calling a function to work
db.commit()

# now, when I run it, it will create the database file


"---------------------------------------------------------------------------------------------------"


# === H0W TO PUT COLUMNS INTO THE TABLE ===

# now to put data in the table:
# use ''' to write on multiple lines
# id is our primary keY

cursor.execute('''
CREATE TABLE IF NOT EXISTS scores(
    id INTEGER,
    mathematics INTEGER,
    english INTEGER,
    physics INTEGER
    );
''')
# MUST NOT FORGET COMMAS OR TABLE WILL BE BROKEN! SYNTAX VERY IMPORTANT

# print table to confirm
print('Table Created!')
# commit to the table. so python knows to update it.
db.commit()


"---------------------------------------------------------------------------------------------------"


# === HOW TO ADD 1 ROW USING VARIABLES ===

# for student 1002, use variables, so you know how to do it if data came from inputs

id_ = 1002
math_ = 71
eng_ = 90
phys_ = 57

# '?' marks are place-holders for the tuple of variables
cursor.execute('INSERT INTO scores '
               'VALUES (?,?,?,?);', (id_, math_, eng_, phys_,))

print('Row added!')
db.commit()


"---------------------------------------------------------------------------------------------------"


# === HOW TO RUN MULTIPLE ROWS IN ONE LINE ===

# make a list of tuples. Each tuple is a student's data. Like a 2d list
# values = [(),(),(),()]
grade1 = [(1003, 76, 60, 68), (1004, 50, 62, 57), (1005, 50, 67, 90)]

# use 'execute many' to add multiple student scores
cursor.executemany('INSERT INTO scores VALUES(?,?,?,?);', grade1)
# confirmations print statement
print('Multiple values added!\n')
db.commit()


"---------------------------------------------------------------------------------------------------"


# === HOW TO VIEW ALL THE DATA IN THE FILE ===

# gets the data from sqlite
cursor.execute('SELECT * FROM scores;')

# this allows me to look at in python
# returns all the data in a list that can be indexed.
data = cursor.fetchall()
print(f'SCORES:\n{data}\n')  # returns data as list [(), (), (), ()]'
print(f'First user: {data[0]}')  # fetches first student's data as a tuple (x,x,x,x)
# don't need DB command because we aren't writing to the database


"---------------------------------------------------------------------------------------------------"


# === HOW TO VIEW THE DATA FROM ONE ROW ===

cursor.execute('SELECT * FROM scores WHERE id = 1004;')

# get from row where student is 1004 - because id is our primary key
student1004 = cursor.fetchone()
print(f'Student 1004 Scores:{student1004}\n')
# don't need DB command because we aren't writing to the database


"---------------------------------------------------------------------------------------------------"


# === HOW TO UPDATE A SPECIFIC VALUE IN THE TABLE

cursor.execute('UPDATE scores SET english = ? WHERE id = 1004;', (54,))
# must up 54 in () with comma so python reads as tuple
db.commit()  # because we are writing to the database

cursor.execute('SELECT * FROM scores WHERE id = 1004;')
# assign data to variable
updated_1004 = cursor.fetchone()
print(f'Updated 1004 info: {updated_1004}\n')


"---------------------------------------------------------------------------------------------------"


# === HOW TO DELETE DATA FROM THE ROW ===

cursor.execute('DELETE FROM scores WHERE id = 1005;')
print('Row 1005 is deleted.')

# end
