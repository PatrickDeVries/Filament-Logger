from dataclasses import dataclass
import pickle

@dataclass
class spool():
    '''Tracks info about a spool of filament'''
    material: str
    # length: float #meters
    # weight: float #grams
    diameter: float #mm
    used: float #meters
    minTemp: int #C
    maxTemp: int #C
    preferredTemp: int #C
    color: str 
    brand: str 
    logFile: str #path
    ID: str
    length: float=None
    weight:float=None
    
    # def __init__(self, m, d, u, min, max, pref, c, b, logf, i, l=None, w=None):
    #     material = m
    #     length = l
    #     diameter = d
    #     used = u
    #     minTemp = min
    #     maxTemp = max
    #     preferredTemp = pref
    #     color = c
    #     brand = b
    #     logFile = logf
    #     ID = i
    
    def printToFile(self, path):
        f = open(path, 'wb')
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
    
    
    