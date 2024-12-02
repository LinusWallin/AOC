from InputReader import InputReader
import numpy as np


def splitData(data):
    dataMat = []
    for row in data:
        dataMat.append(list(map(int, row.split(" "))))
    return dataMat


def direction(levels, i=0):
    direction = levels[i + 1] - levels[i]
    if direction == 0:
        return 0
    elif abs(direction) > 3:
        return 0
    elif direction > 0:
        return 1
    else:
        return -1


def checkLevel(levels):
    removedLevel = False
    startDir = direction(levels)
    if startDir == 0:
        levels.pop(1)
        removedLevel = True
        startDir = direction(levels)
    l = 1
    while l < len(levels) - 1:
        dir = direction(levels, l)
        if dir != startDir:
            if not removedLevel:
                levels.pop(l + 1)
                removedLevel = True
            else:
                return 0
        else:
            l += 1
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
