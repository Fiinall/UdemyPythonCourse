from Database import *
from time import sleep
print("""
Welcome to Information Management System of Marmara University

Here you can create and managa all data of students
Please select process type ;
1. Add Student
2. Ask for list of all students with their all informations.
3. Ask for just name list
4. Ask for information of students who are in specified class
5. Undergraduate Transfer
6. One year update


To quit press q while choosing process type

""")
print("Information table is creating...")
sleep(0.1)
create_table()
print("Information table is ready to process")

while True:
    i = int(input("Which process would u like to do ? "))

    if (i == 1):
        print("You are giong to add student to informations table. \n Please enter .ID,name,surname,faculty,department,class respectively")
        ID = (input("ID : "))
        name = input("Name : ")
        surname = input("Surname : ")
        faculty = input("Faculty : ")
        department = input("Department : ")
        clas = input("Class : ") # Because of class is a embaded function, "clas" is being used.
        add_student(ID,name,surname,faculty,department,clas)

    elif (i == 2):
        print("Student informations is opening...")
        get_student()

    elif (i == 3):
        get_names()

    elif (i == 4):
        clas = int(input("Please enter class you ask for"))
        get_class(clas)

    elif (i == 5):
        print("Undergraduate transfer processes starting...")
        sleep(0.5)
        ID = int(input("Please enter ID of the undergraduate transfer student"))
        new_fac = input("Please enter new faculty of selected student.")
        new_dep = input("Please enter new department of selected student")
        undergraduate_transfer(new_fac,new_dep,ID)

    elif (i == 6):
        oneyearpass()




