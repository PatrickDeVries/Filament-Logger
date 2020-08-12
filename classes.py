from dataclasses import dataclass
import pickle

@dataclass
class spool():
    '''Tracks info about a spool of filament'''
    material: str
    # length: float #meters
    # weight: float #grams
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
        f = open(path, 'rb')
        self = pickle.load(f)
        return self
    
@dataclass
class gcode:
    name: str
    length: float #meters
    spoolID: int
    timesPrinted: int
    ID: str
    
    
    