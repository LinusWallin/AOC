from InputReader import InputReader
import numpy as np


def findGuard(data: list[list[str]], movement: list[str]):
    for i in range(len(data)):
        for j in range(len(data[0])):
            mapObj = data[i][j]
            if mapObj in movement:
                return [i, j]
    return None


def getGuardDir(moveIdx: int):
    return np.array([-np.cos(moveIdx * np.pi / 2), np.sin(moveIdx * np.pi / 2)]).astype(
        int
    )


def guardMovement(data: list[list[str]], movement: list[str], interference: bool):
    pos = np.array(findGuard(data, movement))
    guardMoveIdx = movement.index(data[pos[0]][pos[1]])
    guardDir = getGuardDir(guardMoveIdx)
    if interference:
        if guardMoveIdx % 2 == 0:
            data[pos[0]][pos[1]] = "|"
        else:
            data[pos[0]][pos[1]] = "-"
    else:
        data[pos[0]][pos[1]] = "X"
    active = True
    nextPos = pos
    while active:
        nextPos = (nextPos + guardDir).astype(int)
        if (
            nextPos[0] < len(data)
            and nextPos[0] >= 0
            and nextPos[1] < len(data[0])
            and nextPos[1] >= 0
        ):
            nextSpace = data[nextPos[0]][nextPos[1]]
            if nextSpace != "#":
                if interference:
                    if guardMoveIdx % 2 == 0:
                        if nextSpace == "-":
                            data[nextPos[0]][nextPos[1]] = "+"
                        else:
                            data[nextPos[0]][nextPos[1]] = "|"
                    else:
                        if nextSpace == "|":
                            data[nextPos[0]][nextPos[1]] = "+"
                        else:
                            data[nextPos[0]][nextPos[1]] = "-"
                else:
                    data[nextPos[0]][nextPos[1]] = "X"
            else:
                nextPos = (nextPos - guardDir).astype(int)
                if interference:
                    data[nextPos[0]][nextPos[1]] = "+"
                guardMoveIdx = (guardMoveIdx + 1) % len(movement)
                guardDir = getGuardDir(guardMoveIdx)
        else:
            active = False
            return data


def getVisitedLocations(data: list[list[str]]):
    visited = 0
    for row in data:
        visited += row.count("X")
    return visited


def possibleObstacles(data: list[list[str]]):
    currentPairs = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "#":
                currentPairs[f"{i}, {j}"] = []
                if i+1 < len(data) and j+1 < len(data[0]):
                    for k in range(j+1, len(data[0])):
                        if data[i+1][k] == "#":
                            currentPairs[f"{i}, {j}"].append([i+1, k])
                if j-1 >= 0 and i+1 < len(data):
                    for l in range(i+1, len(data)):
                        if data[l][j-1] == "#":
                            currentPairs[f"{i}, {j}"].append([l, j-1])
    for obstacle in currentPairs.keys():
        if currentPairs[obstacle] == []:
            pass
        else:
            for pair in currentPairs[obstacle]:
                pairKey = f"{pair[0]}, {pair[1]}"
                secondPair = currentPairs[pairKey]
                if secondPair == []:
                    pass
                else:
                    print(pairKey, currentPairs[pairKey])



if __name__ == "__main__":
    inputReader = InputReader(6, True)
    data = inputReader.ReadInput("\n")
    dataMat = [list(row) for row in data]
    movement = ["^", ">", "v", "<"]
    #positionData = guardMovement(dataMat, movement, False)
    #print(getVisitedLocations(positionData))
    positionData2 = guardMovement(dataMat, movement, True)
    for row in positionData2:
        print("".join(row))
    possibleObstacles(positionData2)

