from classes import gcode, spool
import pandas as pd 

def addSpool(spools):
    # print('current', spools)
    while (True):
        try:
            m = input('What is the material? (enter "x" to cancel)\n')
            if m == 'x':
                break
            d = float(input('What is the diameter of the filament (mm)?\n'))
            choice = input('Log use by 1. Weight or 2. Length?\n')
            if choice == '1':
                o = float(input('What is the original weight of the filament (g)?\n'))
                u = float(input('How much filament has been used (g)?\n'))
                typ = 'W'
            elif choice == '2':    
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
            print('\nWhich spool is this gcode sliced for?')
            for i, sp in enumerate(spools):
                print("{}. {}".format(str(i), sp.ID))
            snum = input('''Enter a number. (enter "x" to cancel)\n''')
            if snum == 'x':
                break
            else:
                snum = int(snum)
            
            spid = spools[snum].ID 
            if spools[snum].useType == 'W':
                u = float(input('What is the approximate weight of the print (g)?\n'))
            elif spools[snum].useType == 'L':
                u = float(input('What is the approximate length of the print (m)?\n'))
            pd = 0
            i = input("Enter a unique string that will identify this gcode to you.\n")
            
            newGcode = gcode(u, spid, pd, i, spools[snum].useType)
            choice = input("Has this gcode been scaled? y/n\n")
            if choice.lower().strip() == 'y':
                xsc = float(input('What percent is the x scaling?\n'))
                newGcode.xScale = xsc
                ysc = float(input('What percent is the y scaling?\n'))
                newGcode.yScale = ysc
                zsc = float(input('What percent is the z scaling?\n'))
                newGcode.zScale = zsc     
                       
            newGcode.pickleDump = newGcode.ID + '_gpickle.p'
            gcodes.append(newGcode)
            print('added gcode')
            break
        except:
            print('Input Error')
    return gcodes

def logPrint(gcodes, spools):
    print('Which gcode would you like to log a print for?')
    for i, g in enumerate(gcodes):
        print('{}. {}'.format(i, g.ID))
    gid = int(input('Enter a number.\n'))
    for i, sp in enumerate(spools):
        if sp.ID == gcodes[gid].spoolID:
            spid = i
    choice = input('Log a print for "{}" with spool "{}"? y/n\n'.format(gcodes[gid].ID, spools[spid].ID))
    if choice.strip().lower() == 'y':
        spools[spid].logPrint(gcodes[gid])
        print('\nLogged print')
        if spools[spid].useType == 'W':
            unit = 'g'
        elif spools[spid].useType == 'L':
            unit = 'm'
        print('Spool "{}" has {}{} of filament remaining.'.format(spools[spid].ID, (spools[spid].oSize - spools[spid].used), unit))
        
    
    
def showSpools(spools):
    active = True
    while(active):
        for i, sp in enumerate(spools):
            print("{}. {}".format(str(i), sp.ID))
        choice = input('For details on a spool, enter its number. Enter anything else to return to options.\n')
        active = False
        for i, sp in enumerate(spools):
            if choice == str(i):
                active = True
                sp.printDetails()        

def showGcodes(gcodes):
    active = True
    while(active):
        for i, g in enumerate(gcodes):
            print("{}. {}".format(str(i), g.ID))
        choice = input('For details on a gcode, enter its number. Enter anything else to return to options.\n')
        active = False
        for i, g in enumerate(gcodes):
            if choice == str(i):
                active = True
                g.printDetails() 
                
def showLog(spools):
    active = True
    while(active):
        for i, sp in enumerate(spools):
            print("{}. {}".format(str(i), sp.ID))
        choice = input('''To view a spool's log, enter its number. Enter anything else to return to options.\n''')
        active = False
        for i, sp in enumerate(spools):
            if choice == str(i):
                active = True
                sp.viewLog()  

def saveState(spools, gcodes):
    # Print current spool info
    f = open('./known_spools.csv', 'w')
    for s in spools:
        s.printToFile()
        print(s.pickleDump, file=f)
        
    # Print current gcode info
    f = open('./known_gcodes.csv', 'w')
    for g in gcodes:
        g.printToFile()
        print(g.pickleDump, file=f)

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
