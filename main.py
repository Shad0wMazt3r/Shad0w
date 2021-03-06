import os
import subprocess
import platform
import time
import datetime
print("You are running",platform.system())
while platform.system() == "Windows":
    start = input("$had0w:")
    if start == "view":
        os.system("dir")
    elif start == "help":
        print("""
        1.view        - Shows the files and folders in the directory
        2.clear       - Clears the screen
        3.time        - Shows the date and time
        4.run         - Runs files
        5.make folder - makes a folder
        6.make file   - makes a file
        7.edit        - edit a text file
        8.old         - goes to cmd
        9.back        - goes a folder back
        10.go to      - goes to a specific folder""")
    elif start == "clear":
        os.system("cls")
    elif start == "exit":
       print("To exit press Ctrl + C and press enter")
    elif start == "time":
        print(datetime.datetime.now())
    elif start == "run":
        fo = input("Enter filename with proper commands eg. python main.py:")
        os.system(fo)
    elif start == "":
        continue
    elif start == "make folder":
        name = input("Enter the name of the folder:")
        os.system("mkdir "+name)
    elif start == "make file":
        filename = input("Enter the name of the file:")
        os.system("echo “” >>"+filename)
    elif start == "edit":
        filenameedit = input("Enter the name of the file:")
        os.system("notepad "+filenameedit)
    elif start == "old":
        os.system("cmd")
    elif start == "back":
        os.chdir("..")
    elif start == "go to":
        goto = input("Enter the name of folder to go to:")
        os.chdir(goto)
    else:
        print(start,"is not a command in this shell. Use help to view the commands")
while platform.system().startswith("linux"):
    os.system("cd oslinux && python3 main.py")
