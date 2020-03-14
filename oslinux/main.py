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
        1.view - Shows the files and folders in the directory
        2.clear - Clears the screen
        3.time - Shows the date and time""")
    elif start == "clear":
            os.system("clear")
    elif start == "exit":
        print("To exit press Ctrl + C and press enter")
    elif start == "time":
        print(datetime.datetime.now())
    elif start == "run":
        fo = input("Enter filename with proper commands eg. python main.py:")
        os.system(fo)
    elif start == "":
        continue
    else:
        print(start+" is not a command in this shell. Use help to know about the commands")
while platform.system().startswith("Windows"):
    os.system("cd .. && python main.py")
