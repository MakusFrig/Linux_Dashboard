from subprocess import Popen, PIPE

from tkinter import *

import time

import os


root = Tk()
root.geometry('210x160+1370+700')

root.config(bg = '#ff0000')

root.resizable(False, False)

root.overrideredirect(True)
#this gets rid of te bar on top


root.wait_visibility(root)
root.attributes('-alpha', 0.6)



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

def kb_gb(x):
    return round(x*(9.536743164*10**-7), 3)

def get_info():
    global info_label
    

    pipe = Popen('cat /proc/meminfo', stdout=PIPE, stderr=None, shell=True)

    mem = pipe.communicate()[0].decode('utf-8').split("\n")[:3]
    pipe = Popen('cat /proc/meminfo', stdout=PIPE, stderr=None, shell=True)
    swap = pipe.communicate()[0].decode('utf-8').split("\n")[14:16]

    pipe = Popen('cat /proc/cpuinfo', stdout=PIPE, stderr=None, shell=True)

    cpu = pipe.communicate()[0].decode('utf-8').split("\n")
    for i in range(len(cpu)):
        cpu[i] = cpu[i].split(":")

    cpukeys = []



    core = []

    for i in cpu:
        if i[0] == "cpu MHz\t\t":
            core.append(i[1])
    for i in range(len(core)):
        core[i] = f"core {i} = " + core[i] + "MHz"



    text = []
    for i in mem:
        text.append(i)
    for i in swap:
        text.append(i)

    temp = ""

    for each_line in text:
        temp_line = each_line.replace(" ", "").split(":")
        num = kb_gb(int(temp_line[1].split("k")[0]))

        temp+=f'{temp_line[0]}\t{num}GB\n'

    for i in core:
        temp += f"{i}\n"

    text = temp
    
    info_label.delete('1.0', END)
    info_label.insert('1.0', text)

def end_script(event):
    quit()
    return None

get_info()

exit.place(x = 198, y = 138)

info_label.place(x = 0, y =0)


root.bind('<Delete>', end_script)


while True:

    get_info()
    root.update()
    time.sleep(1)

