# importing essential GUI, database and popup message tools
from tkinter import *
from tkinter import messagebox
import mysql.connector

# WHOLE LOGIC AND FUNCTIONING BACKEND:

# INSERT METHOD: read data provided by user
def insertData():
# insert data provided by user
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

# data validation for a warning message If empty data is provided by user
    if(id =="" or name =="" or dept ==""):
# different type of message box: showwarning
        messagebox.showwarning("Cannot Insert", "All the fields required!")
    else:
# accessing database
        myDB = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="timemachine",
            database="employee")
# inserting data in the empDetails table then commiting it
        myCur = myDB.cursor()
        myCur.execute("insert into empDetails values('"+ id +"','"+ name +"','"+ dept +"') ")
        myDB.commit()
# once inserted we clear the data from entry field using delete() method
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end",)
        show() # added call to show data in listbox
# different type of message box: showinfo
        messagebox.showinfo("Insert Status:", "Data Inserted Successfully!")
        myDB.close()


# UPDATE METHOD: update data provided by user
def updateData():
#read data provided by user
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

# data validation for a warning message If empty data is provided by user
    if (id == "" or name == "" or dept == ""):

# different type of message box: showwarning
        messagebox.showwarning("Cannot Insert", "All the fields required!")
    else:
# acessing database
        myDB = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="timemachine",
            database="employee")
# updating data in the empDetails table then commiting it
        myCur = myDB.cursor()
        myCur.execute("update empDetails set empName='" + name + "', empDept='" + dept + "' where empId='"+ id + "'")
        myDB.commit()
# once inserted we clear the data from entry field using delete() method
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end",)
        show()# added call to show data in listbox
# different type of message box: showinfo
        messagebox.showinfo("Update Status:", "Data Updated Successfully!")
        myDB.close()


# FETCH METHOD: fetch data provided by user
def getData():
# combining reading and checking for empty data
    if(enterId.get() == ""):
        messagebox.showwarning("Fetch Status", "Please Provide the EmployeeID to fetch the data")
    else:
# acessing database
        myDB = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="timemachine",
            database="employee")
    myCur = myDB.cursor()
# fetching all desired data using fetch() that returns a tuple
# no data changes, no call to show() method required
    myCur.execute("select * from empDetails where empID='" + enterId.get() + "'")
    rows = myCur.fetchall()
# row by row, fetch using the index number
# put it in the entry widget using the insert() method
    for row in rows:
        enterName.insert(0, row[1])
        enterDept.insert(0, row[2])
    myDB.close()


# DELETE METHOD: delete data provided by user
def deleteData():
# combined reading and checking of empId data
    if(enterId.get() == ""):
        messagebox.showwarning("Cannot Delete", "Please provide the Emp ID to delete the data")
# delete selected record matching the empID
    else:
        # acessing database
        myDB = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="timemachine",
            database="employee")
        myCur = myDB.cursor()
# deleting all desired data using delete where mysql commands, on specific fields according to ID
        myCur.execute("delete from empDetails where empID='" + enterId.get() + "'")
        myDB.commit()

# clearing data from all fields
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")
        show() # added call to show data in listbox
# show status on a message box
        messagebox.showinfo("Delete Status", "Data Deleted Successfully")
        myDB.close()

# SHOW method: continuously show the data in the database in the list box
def show():
    # acessing database
    myDB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="timemachine",
        database="employee")
    myCur = myDB.cursor()
    myCur.execute("select * from empDetails")
    rows = myCur.fetchall()
    showData.delete(0, showData.size())
    for row in rows:
        addData = str(row[0]) + '     ' + row[1] + '     ' + row[2]
        showData.insert(showData.size() + 1, addData)
    myDB.close()

# creating a reset fields assigned to reset button
def resetFields():
    enterId.delete(0 , "end")
    enterName.delete(0, "end")
    enterDept.delete(0, "end")


# ------------- WHOLE GUI CODE -------------

#creating parent window at the required size with the right label
window = Tk()
window.geometry("700x400")
window.title("Employee CRUD App")

# creating all labels
empId = Label(window, text="Employee ID", font=("Serif", 12))
empId.place(x=20, y=30)

empName = Label(window, text="Employee Name", font=("Serif", 12))
empName.place(x=20, y=60)

empDept = Label(window, text="Employee Dept", font=("Serif", 12))
empDept.place(x=20, y=90)

#creating entry fields to respective labels
enterId = Entry(window)
enterId.place(x=170, y=30)

enterName = Entry(window)
enterName.place(x=170, y=60)

enterDept = Entry(window)
enterDept.place(x=170, y=90)

#adding buttons to perform CRUD operations and a reset button

#Using the command option we specify the method that will be called when clicked
insertBtn = Button(window, text="Insert", font=(
    "Sans", 11), bg="white", command=insertData) # will interact with specific method
insertBtn.place(x=20, y=160)

updateBtn = Button(window, text="Update", font=(
    "Sans", 11), bg="white", command=updateData) # will interact with specific method
updateBtn.place(x=80, y=160)

getBtn = Button(window, text="Fetch", font=(
    "Sans", 11), bg="white", command=getData) # will interact with specific method
getBtn.place(x=150, y=160)

deleteBtn = Button(window, text="Delete", font=(
    "Sans", 11), bg="white", command=deleteData) # will interact with specific method
deleteBtn.place(x=210, y=160)

resetBtn = Button(window, text="Reset", font=(
    "Sans", 11), bg="white", command=resetFields) # will interact with specific method
resetBtn.place(x=20, y=210)

# final listbox widget, it will show the database table
showData = Listbox(window)
showData.place(x=330, y=30)
show()# added call to show data in listbox

#loop till and event
window.mainloop()
