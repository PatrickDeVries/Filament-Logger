from utilities import *

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
