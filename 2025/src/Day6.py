from InputReader import InputReader

def createGrid(data: list[str]) -> list[list[str]]:
    grid = []
    for row in data:
        grid.append([item for item in row.split(" ") if item != ''])
    return grid


def findTotal(data: list[str]) -> int:
    total = 0
    g = createGrid(data)
    for col in range(len(g[0])):
        rowTotal = int(g[0][col])
        for row in range(1, len(g) - 1):
            if g[-1][col] == "*":
                rowTotal *= int(g[row][col])
            else:
                rowTotal += int(g[row][col])
        total += rowTotal
    return total

def findSpecialTotal(data: list[str]) -> int:
    total = 0
    operations = [item for item in data[-1].split(" ") if item != '']
    rowLen = len(data[0])
    operationCount = 0
    t = 0
    for i in range(rowLen - 1, -1, -1):
        num = ""
        for row in range(0, len(data) - 1):
            num += data[row][i]
        num = num.strip()
        if (num.isdigit()):
            if operationCount == 0:
                t = int(num)
                operationCount += 1
            else:
                operationCount += 1
                if operations[-1] == "+":
                    t += int(num)
                else:
                    t *= int(num)
        elif (operationCount != 0):
            operationCount = 0
            total += t
            operations.pop()
    total += t
    return total

if __name__ == "__main__":
    inputReader = InputReader(6, False)
    data = inputReader.ReadInput("\n")
    print(findTotal(data))
    print(findSpecialTotal(data))