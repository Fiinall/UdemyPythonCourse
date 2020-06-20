import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS bookshelf ( Name TEXT,Author TEXT, Publisher TEXT, Papercount INT)")
    connection.commit()
def add_data():
    cursor.execute("Insert into bookshelf Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    connection.commit()
def add_data2(name,author,publisher,pagecount):
    cursor.execute("Insert into bookshelf Values(?,?,?,?)",(name,author,publisher,pagecount))
    connection.commit()
def get_data(): # with this method we take all the info's from bookshelf
                # this is works for all element in data
    cursor.execute("Select * From bookshelf")
    list = cursor.fetchall()
    print("Book Info's")
    a = 1
    for i in list:
        print("book {} is:".format(a),i)
        a += 1

def get_data2(): # with this method we call just name % autohr info's from bookshelf
                 # this is works for all element in data
    cursor.execute("Select Name,Author From bookshelf")
    list = cursor.fetchall()
    print("Book Info's")
    a = 1
    for i in list:
        print("book {} is:".format(a), i)
        a += 1

def get_data3(publisher): # this method gives filtered data because we used "where" in code
                          # It gaves all info's about datas which are pass from filter.
                          # because we did'n mentione like "get Name,Papercount etc.

    cursor.execute("Select * From bookshelf where Publisher = ?",(publisher,))
    list = cursor.fetchall()
    print("Book Info's")
    a = 1
    for i in list:
        print("book {} is:".format(a), i)
        a += 1

def uptade_data(old_publisher,new_publisher):
    cursor.execute("Update bookshelf set Publisher = ? where Publisher = ?",(new_publisher,old_publisher))
    connection.commit()

def delete_data(author):
    cursor.execute("Delete From bookshelf where Author = ?",(author,))
    connection.commit()
#name = input("Name:")
#author = input("Author:")
#publisher = input("Publisher:")
#pagecount = int(input("Papercount:"))

#add_data2(name,author,publisher,pagecount)

get_data()

#get_data2()

#get_data3("inal's in da house")

#uptade_data("inal'sindahouse","inals")

delete_data("Abim")



connection.close()