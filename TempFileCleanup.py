from Tkinter import *
import subprocess
import os
#tkinter import - os are libraries that are called into play to all us to use subprocess, check_call and frames
master = Tk()
master.title("Jarvis Support Tool")
master.geometry("300x100")
#Popen allows for the use of Win Dos commands to run
#cmd calls cmd.exe
#/K tells cmd.exe to run the next commands
#del bla bla bla deletes all* temp files that are not in use
def cleanTemp():subprocess.Popen(['cmd', '/K', 'del /q/f/s %TEMP%\*'])
def cleanDisk():subprocess.check_call(['cleanmgr.exe', '/d', '/sagerun:1'])
#Check_call looks for the program and runs it with what ever options after commas
#Below are variables that buttons are being stored into and the .pack is "Embedding" the code per se
b = Button(master, text="Clean Temp Files", command=cleanTemp)
b.pack()
c = Button(master, text="Clean Disk", command=cleanDisk)
c.pack()
mainloop()
#mainloop here makes this whole process stay alive even after an option is selected. Otherwise it would close upon button selection
#Developed by JM
