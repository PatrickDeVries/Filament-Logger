from classes import gcode, spool
import pandas as pd 

def addSpool(spools):
    print('current', spools)
    while (True):
        try:
            m = input('What is the material?\n')
            d = float(input('What is the diameter of the filament (mm)?\n'))
            choice = input('Log use by 1. Weight or 2. Length?\n')
            if choice == '1':
                o = float(input('What is the original weight of the filament (g)?\n'))
                u = float(input('How much filament has been used (g)?\n'))
                typ = 'W'
            elif choice == '1':    
                o = float(input('What is the original length of the filament (m)?\n'))
                u = float(input('How much filament has been used (m)?\n'))
                typ = 'L'

            minT = int(input('What is the minimum temperature (C)?\n'))
            maxT = int(input('What is the maximum temperature (C)?\n'))
            prefT = int(input('What is your preferred temeperature (C)?\n'))
            c = input('What color is the filament?\n')
            b = input('What brand is the filament?\n')
            i = input('Enter a string that will identify this spool to you.\n')
            
            newSpool = spool(m, d, o, u, minT, maxT, prefT, c, b, i, typ)
            newSpool.pickleDump = i + '_pickle.p'
            newSpool.logFile = i + '_log.txt'

            spools.append(newSpool)
            print('Added spool')

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
print(spools)
if choice == '1':
    spools = addSpool(spools)

print(spools)



# Print current spool info
f = open('./known_spools.csv', 'w')
for s in spools:
    s.printToFile()
    print(s.pickleDump, file=f)
    # f.write(s.pickleDump + '\n')