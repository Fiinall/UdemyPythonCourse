import sqlite3
from time import sleep
connection = sqlite3.connect("bys")
cursor = connection.cursor()
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS infobook (ID INT, name TEXT, surname TEXT, faculty TEXT, department TEXT,class INT)")
    connection.commit()

def add_student(ID,name,surname,faculty,department,clas):
    cursor.execute("Insert into infobook Values(?,?,?,?,?,?)",(ID,name,surname,faculty,department,clas))
        # I can not write class so for this function we can indicate with "clas"
    connection.commit()
    print("Student adding...")
    sleep(0.5)
    print(name,surname,"Added.")

def get_student():
        # If you want to get all the list of student with their informations use this function
    cursor.execute("Select * From infobook")
    list = cursor.fetchall()
    print("All Students Informastion Table")
    a = 1
    for i in list:
        print("Student {} : ".format(a),i)
        a += 1

def get_names():
        # If you want to get all student's names use this function
    cursor.execute("Select name,surname From infobook")
    list = cursor.fetchall()
    print(" Student Name & Surname Table")
    a = 1
    for i in list:
        print("Student {} : ".format(a),i)
        a += 1

def get_class(clas):
        # this function gives you all student of specified class
        # for instance, you can get all 3rd class students
    cursor.execute("Select * From infobook where class = ?",(clas,)) # The last comma here is really required ?
                                                                     # If it is, Why ?
    list = cursor.fetchall()
    print("Student at {}. Class Table".format(clas))
    a = 1
    for i in list:
        print("Student {} : ".format(a),i)
        a += 1


def undergraduate_transfer(new_fac,new_dep,ID):
    # This function can be used for undergraduate transfer process.
    # This function takes whoever you selecet and change their faculties and departments.
    print("Processing...")
    cursor.execute("Update infobook set faculty = ? where ID = ?",(new_fac,ID))
    cursor.execute("Update infobook set department = ? where ID = ?",(new_dep,ID))
    connection.commit()
    sleep(1)
    print("Undergraduate Transfer Process Is Done Successfully")


def oneyearpass():
    cursor.execute("Select class From infobook")
    list1 = cursor.fetchall() # py : past year. py is a list
    ny = list(map(lambda x:x+1 , list1)) # ny : new year.

    cursor.execute("Update infobook set class = ?",(ny))
    connection.commit()

def update():
    # Please implement a function that updates student information
    print("This function will be implemented")
    


