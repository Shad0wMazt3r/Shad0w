import os
import subprocess
import platform
import time
import datetime
print("You are running",platform.system())
while platform.system().startswith("linux"):
    start = input("$had0w:")
    if start == "view":
            os.system("ls")
    elif start == "help":
        print("""
        1.view        - Shows the files and folders in the directory
        2.clear       - Clears the screen
        3.time        - Shows the date and time
        4.run         - Runs files
        5.make folder - makes a folder
        6.make file   - makes a file
        7.edit        - edit a text file
        8.old         - goes to cmd""")
    elif start == "clear":
            os.system("clear")
    elif start == "exit":
        print("To exit press Ctrl + C and press enter")
    elif start == "time":
        print(datetime.datetime.now())
    elif start == "run":
        fo = input("Enter filename with proper commands eg. python main.py:")
        os.system(fo)
    elif start == "make folder":
        name = input("Enter the name of the folder:")
        os.system("mkdir "+name)
    elif start == "make file":
        filename = input("Enter the name of the file:")
        os.system("echo “” >>"+filename)
    elif start == "edit":
        filenameedit = input("Enter the name of the file:")
        os.system("nano "+filenameedit)
    elif start == "old":
        os.system("bash")
    elif start == "back":
        os.chdir("..")
    elif start == "go to":
        goto = input("Enter the name of folder to go to:")
        os.chdir(goto)
    elif start == "":
        continue
    else:
        print(start+" is not a command in this shell. Use help to know about the commands")
while platform.system().startswith("Windows"):
    os.system("cd .. && python main.py")
