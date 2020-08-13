from dataclasses import dataclass
from datetime import datetime
import pickle

@dataclass
class spool():
    '''Tracks info about a spool of filament'''
    material: str
    diameter: float #mm
    oSize: float #m or g
    used: float #m or g
    minTemp: int #C
    maxTemp: int #C
    preferredTemp: int #C
    color: str 
    brand: str 
    ID: str
    useType: str
    logFile: str=None #path
    pickleDump: str=None

    
    def printToFile(self):
        f = open(self.pickleDump, 'wb')
        pickle.dump(self, f)
        return self
        
    def readFromFile(path):
        try:
            f = open(path, 'rb')
            self = pickle.load(f)
            return self
        except:
            print('Spool .p file missing')
    
    def printDetails(self):
        print('\n-----------------------------------------------')
        print('Spool: {}'.format(self.ID))
        print('Brand: {}'.format(self.brand))
        print('Color: {}'.format(self.color))
        print('Material: {}'.format(self.material))
        print('Diameter: {}'.format(self.diameter))
        if self.useType == 'W':
            print('Original weight: {}g'.format(self.oSize))
            print('Used: {}g'.format(self.used))
            print('Remaining: {}g'.format(self.oSize - self.used))
        elif self.useType == 'L':
            print('Original length: {}m'.format(self.oSize))
            print('Used: {}m'.format(self.used))
            print('Remaining: {}m'.format(self.oSize - self.used))
        print('Minimum print temp: {}'.format(self.minTemp))
        print('Maximum print temp: {}'.format(self.maxTemp))
        print('Preferred temp: {}'.format(self.preferredTemp)) 
        print('-----------------------------------------------\n')

    def logPrint(self, gc):
        now = datetime.now()
        dateOfPrint = now.strftime("%m/%d/%Y, %H:%M:%S")
        log = open(self.logFile, 'a')
        if gc.useType == 'W':
            unit = 'g'
        elif gc.useType == 'L':
            unit = 'm'
        print('{}: Gcode {} printed using {}{} of filament\n'.format(dateOfPrint, gc.ID, gc.size, unit), file=log)
        gc.timesPrinted = gc.timesPrinted + 1
        self.used = self.used + gc.size
        log.close()
        
    def viewLog(self):
        try:
            log = open(self.logFile, 'r')
            print('-------------------------------------------------------------')
            for line in log.readlines():
                print(line)       
            log.close()
            print('-------------------------------------------------------------')
        except:
            print('No gcode logs for this spool yet.')
        

    
@dataclass
class gcode:
    size: float #m or g
    spoolID: str
    timesPrinted: int
    ID: str
    useType: str
    xScale: float=100
    yScale: float=100
    zScale: float=100
    pickleDump: str=None
    
    def printToFile(self):
        f = open(self.pickleDump, 'wb')
        pickle.dump(self, f)
        return self
        
    def readFromFile(path):
        try:
            f = open(path, 'rb')
            self = pickle.load(f)
            return self
        except:
            print('Gcode .p file missing')
    
    def printDetails(self):
        print('\n-----------------------------------------------')
        print('Gcode: {}'.format(self.ID))
        print('Sliced for spool: {}'.format(self.spoolID))
        if self.useType == 'W':
            print('Weight: {}'.format(self.size))
        elif self.useType == 'L':
            print('Length: {}'.format(self.size))
        print('Times printed: {}'.format(self.timesPrinted))
        print('X Scale (%): {}'.format(self.xScale))
        print('Y Scale (%): {}'.format(self.yScale))
        print('Z Scale (%): {}'.format(self.zScale))
        print('-----------------------------------------------\n')

    
    