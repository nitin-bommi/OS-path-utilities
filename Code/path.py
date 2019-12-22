# playing with file paths and their info.

# importing the necessary libraries.
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

# printing the os name.
print(os.name)

# printing the type of an item. (file / folder)
print("Item exists :" + str(path.exists("textfile.txt")))
print("It is a file :" + str(path.isfile("textfile.txt")))
print("It is a directory :" + str(path.isdir("textfile.txt")))

# finding the real path of the file.
print("Path : " + str(path.realpath("textfile.txt")))

# getting modified time info.
t = time.ctime(path.getmtime("textfile.txt"))
print(t)

# calculating time elapsed since last modification.
td = datetime.datetime.now() - t1
print(td)
