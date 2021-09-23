#python 3.6.9
#This project is built by Riwader Nabhan 
#N A for Out Of Syllabus python course 

from datetime import datetime as date
import time

today = date.now()

print("Project developed by Riwader Nabhan NSS Engineering college")
print ("program executed at ", today.strftime("%c"))


string = input("Enter a string to animate: ")

for c in string:
    print(c, end = "", flush = True)
    time.sleep(0.16)