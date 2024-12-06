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


def guardMovement(data: list[list[str]], movement: list[str]):
    pos = np.array(findGuard(data, movement))
    guardMoveIdx = movement.index(data[pos[0]][pos[1]])
    guardDir = getGuardDir(guardMoveIdx)
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
            if data[nextPos[0]][nextPos[1]] != "#":
                data[nextPos[0]][nextPos[1]] = "X"
            else:
                nextPos = (nextPos - guardDir).astype(int)
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


if __name__ == "__main__":
    inputReader = InputReader(6, False)
    data = inputReader.ReadInput("\n")
    dataMat = [list(row) for row in data]
    movement = ["^", ">", "v", "<"]
    positionData = guardMovement(dataMat, movement)
    print(getVisitedLocations(positionData))
