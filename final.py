import sqlite3
## connection to sqlite3
connection=sqlite3.connect('student.db')
#create cursor object to insert record,create table:
cursor=connection.cursor()

#create table:

table_info="""
create table Student(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)"""

cursor.execute(table_info)
#insert some more records:

cursor.execute('''Insert Into STUDENT values('Prathiksha','Data Science','A',90)''')

cursor.execute('''Insert Into STUDENT values('John','Data Science','A',100)''')

cursor.execute('''Insert Into STUDENT values('Jacob','Data Science','A',86)''')

cursor.execute('''Insert Into STUDENT values('Mukesh','DEVOPS','A',50)''')

cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

#display all the records:
print('The inserted records are')
data=cursor.execute('''SELECT * from STUDENT''')
for row in data:
    print(row)
#commit the changes in the database:

connection.commit()
connection.close()


