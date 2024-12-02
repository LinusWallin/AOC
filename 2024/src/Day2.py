from InputReader import InputReader
import numpy as np

def splitData(data):
    dataMat = []
    for row in data:
        dataMat.append(list(map(int, row.split(" "))))
    return dataMat

def direction(levels, i=0):
    direction = levels[i+1] - levels[i]
    if direction == 0:
        return 0
    elif abs(direction) > 3:
        return 0
    elif direction > 0:
        return 1
    else:
        return -1
        
def checkLevel(level):
    startDir = direction(level)
    if startDir == 0:
        return 0
    for l in range(1,len(level)-1):
        dir = direction(level, l)
        if dir != startDir:
            return 0
    return 1

def safetyCheck(data):
    safeLevels = 0
    for level in data:
        safeLevels += checkLevel(level)
    return safeLevels

if __name__ == "__main__":
    inputReader = InputReader(2, False)
    data = inputReader.ReadInput("\n")
    data = splitData(data)
    print(safetyCheck(data))
