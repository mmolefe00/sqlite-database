# import SQLite
import sqlite3

# === create database sqlite3 connection ===
db = sqlite3.connect('python_programming')

# create cursor
cursor = db.cursor()


print('Database connection established.\n')       # database connection validation statement.
db.commit()                                     # commit command to database


# === create table columns ===
cursor.execute('''
CREATE TABLE IF NOT EXISTS python_programming(
    id INTEGER,
    name TEXT,
    grade INTEGER
    );
''')
print('- Table Created.')     # validation statement
db.commit()                 # commit


# === insert into database ===

# create nested list of student data in order of id, name and grade.
students = [(55, 'Carl Davis', 61), (66, 'Dennis Fredrickson', 88), (77, 'Jane Richards', 78), (12, 'Peyton Sawyer', 45), (2, 'Lucas Brooke', 99)]


# insert all student data with execute many
cursor.executemany('''
INSERT INTO python_programming(id, name, grade) 
VALUES (?,?,?)''', students)

print('- Students added.')      # validation statement
db.commit()                     # commit


# ensure that student data is in table
print("\nALL STUDENTS DATA:")
cursor.execute('''SELECT id, name, grade FROM python_programming;''')
for row in cursor:
    print('\t{0}\t:\t{1}\t:\t{2}'.format(row[0], row[1], row[2]))


# === select all records with a grade between 60 and ninety ===
print("\nSTUDENTS WITH 60 < GRADE > 80:")
cursor.execute('''
SELECT id, name, grade FROM python_programming
WHERE grade > 60 AND grade < 80;''')
for row in cursor:
    print('\t{0}\t:\t{1}\t:\t{2}'.format(row[0], row[1], row[2]))

# === change Carl Davis's grade to 65 ===
cursor.execute('''
UPDATE python_programming
SET grade = ?
WHERE id = 55;''', (65,))

db.commit()                                 # commit
print('\n- Carl Davis Grade Updated to 65.')        # validation statement


# === Delete Dennis Fredrickson's row===
cursor.execute('''DELETE FROM python_programming WHERE id = 66;''')

db.commit()                             # commit
print('- Fredrickson Row Deleted.\n')     # validation statement



# === change grade of all people with an id below than 55 ===
cursor.execute('''
UPDATE python_programming
SET grade = ?
WHERE id < 55;''', (75,))       # change grade to 75 of all students with an ID below 55.

db.commit()     # commit

# output which students had their grades changed - validation statement
cursor.execute('SELECT * FROM python_programming WHERE id < 55;')
updated_grades = cursor.fetchall()
print(f'Updated Grade with ID < 55:\n\t{updated_grades}')

# === show all data after changes ===
print("\nUPDATED STUDENTS DATA:")
cursor.execute('''SELECT id, name, grade FROM python_programming;''')
for row in cursor:
    print('\t{0}\t:\t{1}\t:\t{2}'.format(row[0], row[1], row[2]))

# drop table to restart - (didn't have to do, but it lets output all changes when running the code.)
# can comment this out if necessary.
cursor.execute('''DROP TABLE python_programming;''')
db.commit()

# === close database ===
db.close()
print('\nDatabase closed.')       # validation statement
