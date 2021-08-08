from subprocess import Popen, PIPE

from tkinter import *

import time

import os


root = Tk()
root.geometry('250x60+10+10')

root.config(bg = '#ff0000')

root.resizable(False, False)

root.overrideredirect(True)
#this gets rid of te bar on top


root.wait_visibility(root)
root.attributes('-alpha', 0.7)



root.lift()
root.wm_attributes("-topmost", True)


def exit_on_command():
    global info_label, exit, root
    get_info()
    time.sleep(1)
    info_label.destroy()
    exit.destroy()
    root.destroy()
    os.system('clear')



info_label = Text(master = root,  font = ("Consolas", 10), bg = '#ff0000')

exit = Button(master = root, text = "X",font = ('Consolas', 10), command = exit_on_command, bg = '#ff0000',
    padx = -4, pady = -2, bd = 0,  activebackground = '#ff0000', relief = GROOVE)

def get_info():
    global info_label
    

    pipe = Popen('cat /proc/meminfo', stdout=PIPE, stderr=None, shell=True)

    text = pipe.communicate()[0].decode('utf-8').split("\n")[:3]

    temp = ""

    for each_line in text:
        temp+=each_line
        temp+="\n"
    text = temp
    
    info_label.delete('1.0', END)
    info_label.insert('1.0', text)

def end_script(event):
    quit()
    return None

get_info()

exit.place(x = 239, y = 40)

info_label.place(x = 0, y =0)


root.bind('<Delete>', end_script)


while True:

    get_info()
    root.update()

