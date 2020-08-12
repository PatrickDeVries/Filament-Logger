from classes import gcode, spool
import pandas as pd 

def addSpool(spools):
    # print('current', spools)
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
            newSpool.pickleDump = i + '_spickle.p'
            newSpool.logFile = i + '_log.txt'

            spools.append(newSpool)
            print('Added spool')

            break     
        except:
            print('Input Error')
    return spools

def addGcode(gcodes, spools):
    # print('current', gcodes)
    while(True):
        try:
            print('\nWhich spool is this sliced for?')
            for i, sp in enumerate(spools):
                print("{}. {}".format(str(i), sp.ID))
            snum = input("Enter a number.\n")
            spid = spools[i].ID 
            if spools[i].useType == 'W':
                u = input('What is the approximate weight of the print (g)?\n')
            elif spools[i].useType == 'L':
                u = input('What is the approximate length of the print (m)?\n')
            pd = 0
            i = input("Enter a unique string that will identify this gcode to you.\n")
            
            newGcode = gcode(u, spid, pd, i)
            choice = input("Has this gcode been scaled? y/n\n")
            if choice.lower().strip() == 'y':
                xsc = float(input('What percent is the x scaling?\n'))
                newGcode.xScale = xsc
                ysc = float(input('What percent is the y scaling?\n'))
                newGcode.yScale = ysc
                zsc = float(input('What percent is the z scaling?\n'))
                newGcode.zScale = zsc     
                       
            newGcode.pickleDump = newGcode.ID + '_gpickle'
            gcodes.append(newGcode)
            print('added gcode')
            break
        except:
            print('Input Error')
    return gcodes

# Read known spools
spools = []
f = open('./known_spools.csv', 'r')
for line in f:
    spools.append(spool.readFromFile(line.strip()))
    
# Read known gcodes
gcodes = []
f = open('./known_gcodes.csv', 'r')
for line in f:
    gcodes.append(gcode.readFromFile(line.strip()))

for g in gcodes:
    print(g)

choice = input('What would you like to do?\n1. Add a spool\n2. Add a gcode\n')
if choice == '1':
    spools = addSpool(spools)
elif choice == '2':
    gcodes = addGcode(gcodes, spools)

print(spools)
print(gcodes)



# Print current spool info
f = open('./known_spools.csv', 'w')
for s in spools:
    s.printToFile()
    print(s.pickleDump, file=f)
    
f = open('./known_gcodes.csv', 'w')
for g in gcodes:
    g.printToFile()
    print(g.pickleDump, file=f)
