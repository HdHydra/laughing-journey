#python 3.6.9
#This project is built by Riwader Nabhan 
#N A for Out Of Syllabus python course 

from datetime import datetime as dt
import time as t

x = dt.now()

print("Project developed by Riwader Nabhan NSS Engineering college")
print ("program executed at ",x.strftime("%c"))


w = input("Enter a string to animate: ")

for ch in w:
    print(ch, end = "", flush = True)
    t.sleep(0.16)