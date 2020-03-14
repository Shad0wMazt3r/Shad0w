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
        1.view   - Shows the files and folders in the directory
        2.clear  - Clears the screen
        3.time   - Shows the date and time
        4.run    - runs files""")
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
    else:
        print(start+" is not a command in this shell. Use help to know about the commands")
while platform.system().startswith("linux"):
    os.system("cd oslinux && python3 main.py")