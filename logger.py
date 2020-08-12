from classes import gcode, spool
import pandas as pd 



# sp = spool('PLA', 1.75, 0, 195, 230, 195, 'black', 'MIKA3D', './blackPLA.txt', 'MIKA3D black PLA spool 1', weight=500) 

# sp.printToFile('./spout.p')

# cp = spool.readFromFile('./spout.p')

# print(sp, cp)

spools = []
f = open('./known_spools.csv')
for line in f:
    spools.append(spool.readFromFile(line))
    
for s in spools:
    print(s)
