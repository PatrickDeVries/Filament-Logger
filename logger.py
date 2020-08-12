from classes import gcode, spool
import pandas as pd 

def addSpool(spools):
    print('addSpool')
    while (True):
        try:
            m = input('What is the material?\n')
            d = float(input('What is the diameter of the filament?\n'))
            
            break
        except:
            print('Input Error')
    return spools


# sp = spool('PLA', 1.75, 0, 195, 230, 195, 'black', 'MIKA3D', './blackPLA.txt', 'MIKA3D black PLA spool 1', 'spout.p', weight=500) 

# sp.printToFile()

# cp = spool.readFromFile('./spout.p')

# print(sp, cp)

# Read known spools
spools = []
f = open('./known_spools.csv', 'r')
for line in f:
    spools.append(spool.readFromFile(line.strip()))
    
# for s in spools:
#     print(s)
#     print(s.pickleDump)

choice = input('What would you like to do?\n1. Add a spool\n')

if choice == '1':
    spools = addSpool(spools)







# Print current spool info
f = open('./known_spools.csv', 'w')
for s in spools:
    s.printToFile()
    print(s.pickleDump, file=f)
    # f.write(s.pickleDump + '\n')