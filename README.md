# Linux_Ram_Check
This is my ram checker for the linux operating system.


#Use

There are two ways of using this ram checker

1. Because this is for linux python should be pre installed on many systems, if not, install it. Also make sure that tkinter functions on your linux device as you may need to install some driver. (Tkinter is the gui platform used) Then you can run this from the command line
2. The other way you can run this file is through pyinstaller, the way to do this is as follows<br />```Shell pyinstaller --hidden-import tkiner --onefile ram_check.py ```<br /> Then it will generate a few folders, you can throw away the build folder as well as the pycache, your executable will be in the 'dist folder'
