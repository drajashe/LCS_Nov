# Python GUI – tkinter
- Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter outputs the fastest and easiest way to create the GUI applications. Creating a GUI using tkinter is an easy task.
To create a tkinter:
https://www.geeksforgeeks.org/python-gui-tkinter/

### Importing the module – tkinter
- Create the main window (container)
- Add any number of widgets to the main window
- Apply the event Trigger on the widgets.
- Importing tkinter is same as importing any other module in the python code. Note that the name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x is ‘tkinter’.

import tkinter
There are two main methods used you the user need to remember while creating the Python application with GUI.



- Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1): To create a main window, tkinter offers a method ‘Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)’. To change the name of the window, you can change the className to the desired one. The basic code used to create the main window of the application is:
m=tkinter.Tk() where m is the name of the main window object

- mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
m.mainloop()


import tkinter
m = tkinter.Tk()
'''
widgets are added here
'''
m.mainloop()


- tkinter also offers access to the geometric configuration of the widgets which can organize the widgets in the parent windows. There are mainly three geometry manager classes class.

    - pack() method:It organizes the widgets in blocks before placing in the parent widget.
    - grid() method:It organizes the widgets in grid (table-like structure) before placing in the parent widget.
    - place() method:It organizes the widgets by placing them on specific positions directed by the programmer.


There are a number of widgets which you can put in your tkinter application. Some of the major widgets are explained below:

- Button:To add a button in your application, this widget is used.
The general syntax is:
w=Button(master, option=value)
master is the parameter used to represent the parent window.
There are number of options which are used to change the format of the Buttons. Number of options can be passed as parameters separated by commas. Some of them are listed below.

- activebackground: to set the background color when button is under the cursor.
- activeforeground: to set the foreground color when button is under the cursor.
- bg: to set he normal background color.
- command: to call a function.
- font: to set the font on the button label.
- image: to set the image on the button.
- width: to set the width of the button.
- height: to set the height of the button.


dit
play_arrow

brightness_5
import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()


### Canvas: It is used to draw pictures and other complex layout like graphics, text and widgets.
The general syntax is:
w = Canvas(master, option=value)
master is the parameter used to represent the parent window.
There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

bd: to set the border width in pixels.
bg: to set the normal background color.
cursor: to set the cursor used in the canvas.
highlightcolor: to set the color shown in the focus highlight.
width: to set the width of the widget.
height: to set the height of the widget.
filter_none
edit
play_arrow

brightness_5
from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()
Output:


CheckButton: To select any number of options by displaying a number of options to a user as toggle buttons. The general syntax is:
w = CheckButton(master, option=value)
There are number of options which are used to change the format of this widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

Title: To set the title of the widget.
activebackground: to set the background color when widget is under the cursor.
activeforeground: to set the foreground color when widget is under the cursor.
bg: to set he normal backgrouSteganography
Break

Secret Code:

Attach a File:nd color.

command: to call a function.
font: to set the font on the button label.
image: to set the image on the widget.
filter_none
edit
play_arrow

brightness_5
from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
mainloop()
Output:


Entry:It is used to input the single line text entry from the user.. For multi-line text input, Text widget is used.
The general syntax is:


# Python | Writing to an excel file using openpyxl module
Prerequisite : Reading an excel file using openpyxl

- Openpyxl is a Python library for reading and writing Excel (with extension xlsx/xlsm/xltx/xltm) files. The openpyxl module allows Python program to read and modify Excel files.

For example, user might have to go through thousands of rows and pick out few handful information to make small changes based on some criteria. Using Openpyxl module, these tasks can be done very efficiently and easily.



 

Let’s see how to create and write to an excel-sheet using Python.

## Code #1 : Program to print a active sheet title name

filter_none
edit
play_arrow

brightness_5
### import openpyxl module 
import openpyxl 
  
### Call a Workbook() function of openpyxl  
### to create a new blank Workbook object 
wb = openpyxl.Workbook() 
  
### Get workbook active sheet   
### from the active attribute.  
sheet = wb.active 
  
### Once have the Worksheet object, 
### one can get its name from the 
### title attribute. 
sheet_title = sheet.title 
  
print("active sheet title: " + sheet_title) 
Output :

active sheet title: Sheet
 
Code #2 : Program to change the Title name

filter_none
edit
play_arrow

brightness_5
### import openpyxl module 
import openpyxl 
  
### Call a Workbook() function of openpyxl  
### to create a new blank Workbook object 
wb = openpyxl.Workbook() 
  
### Get workbook active sheet   
### from the active attribute 
sheet = wb.active 
  
### One can change the name of the title 
sheet.title = "sheet1"
  
print("sheet name is renamed as: " + sheet.title) 
Output :

sheet name is renamed as: sheet1
 
Code #3 :Program to write to an Excel sheet

filter_none
edit
play_arrow

brightness_5
### import openpyxl module 
import openpyxl 
  
### Call a Workbook() function of openpyxl  
### to create a new blank Workbook object 
wb = openpyxl.Workbook() 
  
### Get workbook active sheet   
### from the active attribute 
sheet = wb.active 
  
### Cell objects also have row, column 
### and coordinate attributes that provide 
### location information for the cell. 
  
### Note: The first row or column integer 
### is 1, not 0. Cell object is created by 
### using sheet object's cell() method. 
c1 = sheet.cell(row = 1, column = 1) 
  
### writing values to cells 
c1.value = "ANKIT"
  
c2 = sheet.cell(row= 1 , column = 2) 
c2.value = "RAI"
  
### Once have a Worksheet object, one can 
### access a cell object by its name also. 
### A2 means column = 1 & row = 2. 
c3 = sheet['A2'] 
c3.value = "RAHUL"
  
### B2 means column = 2 & row = 2. 
c4 = sheet['B2'] 
c4.value = "RAI"
  
### Anytime you modify the Workbook object 
### or its sheets and cells, the spreadsheet 
### file will not be saved until you call 
### the save() workbook method. 
wb.save("C:\\Users\\user\\Desktop\\demo.xlsx") 
Output :
Output
 

code #4 :Program to add Sheets in the Workbook

filter_none
edit
play_arrow

brightness_5
### import openpyxl module 
import openpyxl 
  
### Call a Workbook() function of openpyxl  
### to create a new blank Workbook object 
wb = openpyxl.Workbook() 
  
sheet = wb.active 
  
### Sheets can be added to workbook with the 
### workbook object's create_sheet() method.  
wb.create_sheet(index = 1 , title = "demo sheet2") 
  
wb.save("C:\\Users\\user\\Desktop\\demo.xlsx") 
Output :
output

# Python GUI – tkinter
- Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter outputs the fastest and easiest way to create the GUI applications. Creating a GUI using tkinter is an easy task.
To create a tkinter:
https://www.geeksforgeeks.org/python-gui-tkinter/

### Importing the module – tkinter
- Create the main window (container)
- Add any number of widgets to the main window
- Apply the event Trigger on the widgets.
- Importing tkinter is same as importing any other module in the python code. Note that the name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x is ‘tkinter’.

import tkinter
There are two main methods used you the user need to remember while creating the Python application with GUI.



- Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1): To create a main window, tkinter offers a method ‘Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)’. To change the name of the window, you can change the className to the desired one. The basic code used to create the main window of the application is:
m=tkinter.Tk() where m is the name of the main window object

- mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
m.mainloop()


import tkinter
m = tkinter.Tk()
'''
widgets are added here
'''
m.mainloop()


- tkinter also offers access to the geometric configuration of the widgets which can organize the widgets in the parent windows. There are mainly three geometry manager classes class.

    - pack() method:It organizes the widgets in blocks before placing in the parent widget.
    - grid() method:It organizes the widgets in grid (table-like structure) before placing in the parent widget.
    - place() method:It organizes the widgets by placing them on specific positions directed by the programmer.


There are a number of widgets which you can put in your tkinter application. Some of the major widgets are explained below:

- Button:To add a button in your application, this widget is used.
The general syntax is:
w=Button(master, option=value)
master is the parameter used to represent the parent window.
There are number of options which are used to change the format of the Buttons. Number of options can be passed as parameters separated by commas. Some of them are listed below.

- activebackground: to set the background color when button is under the cursor.
- activeforeground: to set the foreground color when button is under the cursor.
- bg: to set he normal background color.
- command: to call a function.
- font: to set the font on the button label.
- image: to set the image on the button.
- width: to set the width of the button.
- height: to set the height of the button.


dit
play_arrow

brightness_5
import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()


### Canvas: It is used to draw pictures and other complex layout like graphics, text and widgets.
The general syntax is:
w = Canvas(master, option=value)
master is the parameter used to represent the parent window.
There are number of options which are used to change the format of the widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

bd: to set the border width in pixels.
bg: to set the normal background color.
cursor: to set the cursor used in the canvas.
highlightcolor: to set the color shown in the focus highlight.
width: to set the width of the widget.
height: to set the height of the widget.
filter_none
edit
play_arrow

brightness_5
from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()
Output:


CheckButton: To select any number of options by displaying a number of options to a user as toggle buttons. The general syntax is:
w = CheckButton(master, option=value)
There are number of options which are used to change the format of this widget. Number of options can be passed as parameters separated by commas. Some of them are listed below.

Title: To set the title of the widget.
activebackground: to set the background color when widget is under the cursor.
activeforeground: to set the foreground color when widget is under the cursor.
bg: to set he normal backgrouSteganography
Break

Secret Code:

Attach a File:nd color.

command: to call a function.
font: to set the font on the button label.
image: to set the image on the widget.
filter_none
edit
play_arrow

brightness_5
from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
mainloop()
Output:


Entry:It is used to input the single line text entry from the user.. For multi-line text input, Text widget is used.
The general syntax is:


# Python | Writing to an excel file using openpyxl module
Prerequisite : Reading an excel file using openpyxl

- Openpyxl is a Python library for reading and writing Excel (with extension xlsx/xlsm/xltx/xltm) files. The openpyxl module allows Python program to read and modify Excel files.

For example, user might have to go through thousands of rows and pick out few handful information to make small changes based on some criteria. Using Openpyxl module, these tasks can be done very efficiently and easily.



 

Let’s see how to create and write to an excel-sheet using Python.

## Code #1 : Program to print a active sheet title name

filter_none
edit
play_arrow

brightness_5
### import openpyxl module 
import openpyxl 
  
### Call a Workbook() function of openpyxl  
### to create a new blank Workbook object 
wb = openpyxl.Workbook() 
  
### Get workbook active sheet   
### from the active attribute.  
sheet = wb.active 
  
### Once have the Worksheet object, 
### one can get its name from the 
### title attribute. 
sheet_title = sheet.title 
  
print("active sheet title: " + sheet_title) 
Output :

active sheet title: Sheet
 
Code #2 : Program to change the Title name

filter_none
edit
play_arrow

brightness_5
### import openpyxl module 
import openpyxl 
  
### Call a Workbook() function of openpyxl  
### to create a new blank Workbook object 
wb = openpyxl.Workbook() 
  
### Get workbook active sheet   
### from the active attribute 
sheet = wb.active 
  
### One can change the name of the title 
sheet.title = "sheet1"
  
print("sheet name is renamed as: " + sheet.title) 
Output :

sheet name is renamed as: sheet1
 
Code #3 :Program to write to an Excel sheet

filter_none
edit
play_arrow

brightness_5
### import openpyxl module 
import openpyxl 
  
### Call a Workbook() function of openpyxl  
### to create a new blank Workbook object 
wb = openpyxl.Workbook() 
  
### Get workbook active sheet   
### from the active attribute 
sheet = wb.active 
  
### Cell objects also have row, column 
### and coordinate attributes that provide 
### location information for the cell. 
  
### Note: The first row or column integer 
### is 1, not 0. Cell object is created by 
### using sheet object's cell() method. 
c1 = sheet.cell(row = 1, column = 1) 
  
### writing values to cells 
c1.value = "ANKIT"
  
c2 = sheet.cell(row= 1 , column = 2) 
c2.value = "RAI"
  
### Once have a Worksheet object, one can 
### access a cell object by its name also. 
### A2 means column = 1 & row = 2. 
c3 = sheet['A2'] 
c3.value = "RAHUL"
  
### B2 means column = 2 & row = 2. 
c4 = sheet['B2'] 
c4.value = "RAI"
  
### Anytime you modify the Workbook object 
### or its sheets and cells, the spreadsheet 
### file will not be saved until you call 
### the save() workbook method. 
wb.save("C:\\Users\\user\\Desktop\\demo.xlsx") 
Output :
Output
 

code #4 :Program to add Sheets in the Workbook

filter_none
edit
play_arrow

brightness_5
### import openpyxl module 
import openpyxl 
  
### Call a Workbook() function of openpyxl  
### to create a new blank Workbook object 
wb = openpyxl.Workbook() 
  
sheet = wb.active 
  
### Sheets can be added to workbook with the 
### workbook object's create_sheet() method.  
wb.create_sheet(index = 1 , title = "demo sheet2") 
  
wb.save("C:\\Users\\user\\Desktop\\demo.xlsx") 
Output :
output


# Python | Simple registration form using Tkinter
Prerequisites : Tkinter Introduction, openpyxl module.

Python provides the Tkinter toolkit to develop GUI applications. Now, it’s upto the imagination or necessity of developer, what he/she want to develop using this toolkit. Let’s make a simple information form GUI application using Tkinter. In this application, User has to fill up the required information and that information is automatically written into an excel file.

Firstly, create an empty excel file, after that pass an absolute path of the excel file in the program so that the program is able to access that excel file.



 

Below is the implementation :
filter_none
brightness_5
# import openpyxl and tkinter modules 
from openpyxl import *
from tkinter import *
  
# globally declare wb and sheet variable 
  
# opening the existing excel file 
wb = load_workbook('C:\\Users\\Admin\\Desktop\\excel.xlsx') 
  
# create the sheet object 
sheet = wb.active 
  
  
def excel(): 
      
    # resize the width of columns in 
    # excel spreadsheet 
    sheet.column_dimensions['A'].width = 30
    sheet.column_dimensions['B'].width = 10
    sheet.column_dimensions['C'].width = 10
    sheet.column_dimensions['D'].width = 20
    sheet.column_dimensions['E'].width = 20
    sheet.column_dimensions['F'].width = 40
    sheet.column_dimensions['G'].width = 50
  
    # write given data to an excel spreadsheet 
    # at particular location 
    sheet.cell(row=1, column=1).value = "Name"
    sheet.cell(row=1, column=2).value = "Course"
    sheet.cell(row=1, column=3).value = "Semester"
    sheet.cell(row=1, column=4).value = "Form Number"
    sheet.cell(row=1, column=5).value = "Contact Number"
    sheet.cell(row=1, column=6).value = "Email id"
    sheet.cell(row=1, column=7).value = "Address"
  
  
# Function to set focus (cursor) 
def focus1(event): 
    #set focus on the course_field box 
    course_field.focus_set() 
  
  
# Function to set focus 
def focus2(event): 
    #set focus on the sem_field box 
    sem_field.focus_set() 
  
  
# Function to set focus 
def focus3(event): 
    #set focus on the form_no_field box 
    form_no_field.focus_set() 
  
  
# Function to set focus 
def focus4(event): 
    #set focus on the contact_no_field box 
    contact_no_field.focus_set() 
  
  
# Function to set focus 
def focus5(event): 
    #set focus on the email_id_field box 
    email_id_field.focus_set() 
  
  
# Function to set focus 
def focus6(event): 
    #set focus on the address_field box 
    address_field.focus_set() 
  
  
# Function for clearing the 
# contents of text entry boxes 
def clear(): 
      
    #clear the content of text entry box 
    name_field.delete(0, END) 
    course_field.delete(0, END) 
    sem_field.delete(0, END) 
    form_no_field.delete(0, END) 
    contact_no_field.delete(0, END) 
    email_id_field.delete(0, END) 
    address_field.delete(0, END) 
  
  
# Function to take data from GUI  
# window and write to an excel file 
def insert(): 
      
    # if user not fill any entry 
    # then print "empty input" 
    if (name_field.get() == "" and
        course_field.get() == "" and
        sem_field.get() == "" and
        form_no_field.get() == "" and
        contact_no_field.get() == "" and
        email_id_field.get() == "" and
        address_field.get() == ""): 
              
        print("empty input") 
  
    else: 
  
        #assigning the max row and max column 
        #value upto which data is written 
        #in an excel sheet to the variable 
        current_row = sheet.max_row 
        current_column = sheet.max_column 
  
        #get method returns current text 
        #as string which we write into 
        #excel spreadsheet at particular location 
        sheet.cell(row=current_row + 1, column=1).value = name_field.get() 
        sheet.cell(row=current_row + 1, column=2).value = course_field.get() 
        sheet.cell(row=current_row + 1, column=3).value = sem_field.get() 
        sheet.cell(row=current_row + 1, column=4).value = form_no_field.get() 
        sheet.cell(row=current_row + 1, column=5).value = contact_no_field.get() 
        sheet.cell(row=current_row + 1, column=6).value = email_id_field.get() 
        sheet.cell(row=current_row + 1, column=7).value = address_field.get() 
  
        #save the file 
        wb.save('C:\\Users\\Admin\\Desktop\\excel.xlsx') 
  
        #set focus on the name_field box 
        name_field.focus_set() 
  
        #call the clear() function 
        clear() 
  
  
# Driver code 
if __name__ == "__main__": 
      
    #create a GUI window 
    root = Tk() 
  
    #set the background colour of GUI window 
    root.configure(background='light green') 
  
    #set the title of GUI window 
    root.title("registration form") 
  
    #set the configuration of GUI window 
    root.geometry("500x300") 
  
    excel() 
  
    #create a Form label 
    heading = Label(root, text="Form", bg="light green") 
  
    #create a Name label 
    name = Label(root, text="Name", bg="light green") 
  
    #create a Course label 
    course = Label(root, text="Course", bg="light green") 
  
    #create a Semester label 
    sem = Label(root, text="Semester", bg="light green") 
  
    #create a Form No. lable 
    form_no = Label(root, text="Form No.", bg="light green") 
  
    #create a Contact No. label 
    contact_no = Label(root, text="Contact No.", bg="light green") 
  
    #create a Email id label 
    email_id = Label(root, text="Email id", bg="light green") 
  
    #create a address label 
    address = Label(root, text="Address", bg="light green") 
  
    #grid method is used for placing 
    #the widgets at respective positions 
    #in table like structure . 
    heading.grid(row=0, column=1) 
    name.grid(row=1, column=0) 
    course.grid(row=2, column=0) 
    sem.grid(row=3, column=0) 
    form_no.grid(row=4, column=0) 
    contact_no.grid(row=5, column=0) 
    email_id.grid(row=6, column=0) 
    address.grid(row=7, column=0) 
  
    #create a text entry box 
    #for typing the information 
    name_field = Entry(root) 
    course_field = Entry(root) 
    sem_field = Entry(root) 
    form_no_field = Entry(root) 
    contact_no_field = Entry(root) 
    email_id_field = Entry(root) 
    address_field = Entry(root) 
  
    #bind method of widget is used for 
    #the binding the function with the events 
  
    #whenever the enter key is pressed 
    #then call the focus1 function 
    name_field.bind("<Return>", focus1) 
  
    #whenever the enter key is pressed 
    #then call the focus2 function 
    course_field.bind("<Return>", focus2) 
  
    #whenever the enter key is pressed 
    #then call the focus3 function 
    sem_field.bind("<Return>", focus3) 
  
    #whenever the enter key is pressed 
    #then call the focus4 function 
    form_no_field.bind("<Return>", focus4) 
  
    #whenever the enter key is pressed 
    #then call the focus5 function 
    contact_no_field.bind("<Return>", focus5) 
  
    #whenever the enter key is pressed 
    #then call the focus6 function 
    email_id_field.bind("<Return>", focus6) 
  
    #grid method is used for placing 
    #the widgets at respective positions 
    #in table like structure . 
    name_field.grid(row=1, column=1, ipadx="100") 
    course_field.grid(row=2, column=1, ipadx="100") 
    sem_field.grid(row=3, column=1, ipadx="100") 
    form_no_field.grid(row=4, column=1, ipadx="100") 
    contact_no_field.grid(row=5, column=1, ipadx="100") 
    email_id_field.grid(row=6, column=1, ipadx="100") 
    address_field.grid(row=7, column=1, ipadx="100") 
  
    #call excel function 
    excel() 
  
    #create a Submit Button and place into the root window 
    submit = Button(root, text="Submit", fg="Black", 
                            bg="Red", command=insert) 
    submit.grid(row=8, column=1) 
  
    #start the GUI 
    root.mainloop() 
Output :



