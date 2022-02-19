# This application adds a file to a specified directory then adds personal information before returning the contents of the new file.
import os
import sys

# Collect directory data and try to navigate to it.
dir = os.getcwd() + '\\' + input ("Where would you like to save your file?\n")
try:
    os.chdir(dir)
except:
    print("File does not exist. Please make sure you are running this application from the correct directory.")
    sys.exit()

# Name new file.
fNam = input ("what is the name of the file?\n") + ".txt"

# Collect personal information.
iName = input ("What is your name\n")
addr = input ("What is your address\n")
pNum = input ("What is your phone number?\n")

# Create, write to, and read new file.
file = open(fNam, "w")
file.write ("{}, {}, {}".format(iName,addr,pNum))
file.close()
file = open(fNam, "r")
print(file.read())
file.close()