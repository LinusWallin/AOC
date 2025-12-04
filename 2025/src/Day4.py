from InputReader import InputReader

def createGrid(data: list[str]) -> list[list[str]]:
    grid = []
    for row in data:
        grid.append(list(row))
    return grid

def accessibleRolls(data: list[str], removable:bool) -> int:
    g = createGrid(data)
    xMax = len(g[0]) - 1
    yMax = len(g) - 1
    rolls = 0
    while True:
        removed = 0
        for y in range(len(g)):
            for x in range(len(g[y])):
                if (g[y][x] == "@"):
                    if (checkAdjacentCells(g, x, y, xMax, yMax, removable)):
                        rolls += 1
                        removed += 1
        if (not removable or removed == 0):
            break
    return rolls
            
def checkAdjacentCells(g:int, x:int, y:int, xMax:int, yMax:int, removable:bool) -> bool:
    counter = 0
    for yCoord in range(y-1, y+2):
        if yCoord < 0 or yCoord > yMax:
            continue
        for xCoord in range(x-1, x+2):
            if xCoord < 0 or xCoord > xMax:
                continue
            elif xCoord == x and yCoord == y:
                continue
            if (g[yCoord][xCoord] == "@"):
                counter += 1
    if (counter >= 4):
        return False
    else:
        if (removable):
            g[y][x] = "."
        return True

if __name__ == "__main__":
    inputReader = InputReader(4, False)
    data = inputReader.ReadInput("\n")
    print(accessibleRolls(data, True))
    
