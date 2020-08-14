import tkinter as tk 
from tkinter import ttk 
from utilities import *
from functools import partial

def addSpoolTK(window, mainf, spools):
    f = tk.Frame(window)
    f.grid(row=0, column=0, sticky='news')
    f.tkraise()
    lbl = tk.Label(text='Enter the necessary information here')
    lbl.grid(column=0, row=0)
        
    def ret():
        mainf.tkraise()
        
    rt = tk.Button(text='click to return', command=ret)
    rt.grid(column=0, row=1)

# Read known spools
spools = []
try:
    f = open('./known_spools.csv', 'r')
    for line in f:
        spools.append(spool.readFromFile(line.strip()))
        f.close()
except:
    # print('error loading known spools')
    f = open('./known_spools.csv', 'w')
    f.close()


# Read known gcodes
gcodes = []
f = open('./known_gcodes.csv', 'r')
for line in f:
    gcodes.append(gcode.readFromFile(line.strip()))
f.close()

window = tk.Tk()

window.title("Filament Tracker")
w = int(window.winfo_screenwidth()//2)
h = int(window.winfo_screenheight()//1.5)
window.geometry('{}x{}'.format(w, h))
center(window)


mainf = tk.Frame(window)
mainf.grid(row=0, column=0, sticky='news')
mainf.tkraise()

lbl = tk.Label(mainf, text='''What would you like to do?''')
lbl.grid(column=0, row=0)

addsp = tk.Button(mainf, text='Add a spool', command=partial(addSpoolTK, window, mainf, spools))
addgc = tk.Button(mainf, text='Add a gcode', command=lambda: addGcode(gcodes, spools))
logpr = tk.Button(mainf, text='Log a print', command=lambda: logPrint(gcodes, spools))
viewlog = tk.Button(mainf, text='''View a Spool's log''', command=lambda: showLog(spools))
showsp = tk.Button(mainf, text='View spools', command=lambda: showSpools(spools))
showgc = tk.Button(mainf, text='View gcodes', command=lambda: showGcodes(gcodes))

controls = [addsp, addgc, logpr, viewlog, showsp, showgc]
for i, btn in enumerate(controls):
    btn.grid(column=0, row=i+1)
    btn.configure(height = 5, width=20)
window.mainloop()

while (True):
    choice = input('''What would you like to do? (Enter anything else to exit)\n1. Add a spool\n2. Add a gcode\n3. Log a print\n4. View a Spool's log\n5. Show spools\n6. Show gcodes\n''')
    print('')
    if choice == '1':
        spools = addSpool(spools)
    elif choice == '2':
        gcodes = addGcode(gcodes, spools)
    elif choice == '3':
        logPrint(gcodes, spools)
    elif choice == '4':
        showLog(spools)
    elif choice == '5':
        showSpools(spools)
    elif choice == '6':
        showGcodes(gcodes)
    else:
        break
    saveState(spools, gcodes)



saveState(spools, gcodes)
