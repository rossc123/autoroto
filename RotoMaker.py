# Import necessary modules
import FindMattes as fm
import tkinter as tk
from tkinter import Button, Label, StringVar
from tkinter import filedialog as fd
from os import listdir


# Create the default window
root = tk.Tk()
root.title("AutoRoto")
root.geometry('250x250')
directoryName=StringVar()

#Browse Instructions
file_label=Label(root,text="Please select a directory to Roto")
file_label.pack(anchor='n')

#Function to handle browsing
def browse_button():
    name= fd.askdirectory(parent=root,initialdir="/", title = 'Please select a directory')  
    global directoryName
    directoryName=name
   

#Button to activate browse function
button2 = Button(text="Browse", command=browse_button)
button2.pack(anchor='n',pady=10)

#Label to explain matte sizes
option_label=Label(root,text="Output matte vertical resolution\n (256 recommended for quick tests)")
option_label.pack(anchor='n')

# Create the list of options
options_list = [1080, 720, 480, 256]

# Variable to keep track of the option
# selected in OptionMenu
matteHeight = tk.IntVar(root)

# Set the default value of the variable
matteHeight.set(256)

# Create the optionmenu widget and passing
# the options_list and value_inside to it.
question_menu = tk.OptionMenu(root, matteHeight, *options_list)
question_menu.pack()

#Function to call the ML model and create matte
def makeMatte():
    global matteHeight
    listOfFiles =listdir(directoryName)
    for currentFile in listOfFiles:    
        sourceFile = directoryName +"/"+currentFile    
        mainNameEnd=currentFile.find('.')
        nameForMatte=currentFile[:mainNameEnd]+"_matte" + currentFile[mainNameEnd:]
        fullPathMatte = directoryName +"/"+nameForMatte
        fm.createMatte(sourceFile,fullPathMatte,matteHeight.get())
        var.set("Just created "+nameForMatte)


# Submit button
# Whenever we click the submit button, our submitted
submit_button = tk.Button(root, text='Submit', command=makeMatte)
submit_button.pack(pady=20)

#show successful creation
var=StringVar()
label=Label( root, textvariable=var)
label.pack()

root.mainloop()
