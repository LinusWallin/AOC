from InputReader import InputReader

def findMaxJoltage(data: list[str]) -> int:
    joltage = 0
    for d in data:
        joltageArr = list(map(int, list(d)))
        mInt = max(joltageArr)
        startIdx = joltageArr.index(mInt)
        if (startIdx == len(joltageArr)-1):
            subArr = joltageArr[:-1]
            joltage += int(str(max(subArr)) + str(mInt))
        else:
            subArr = joltageArr[startIdx + 1:]
            joltage += int(str(mInt) + str(max(subArr)))
    return joltage

def findNewMaxJoltage(data: list[str]) -> int:
    joltage = 0
    for d in data:
        joltageArr = list(map(int, list(d)))
        bIdx = []
        lastIdx = -1
        for battery in range(12):
            if battery != 0:
                lastIdx = bIdx[-1]
            bIdx.append(findStart(joltageArr, lastIdx, battery))
        currJoltage = ""
        for idx in bIdx:
            currJoltage += str(joltageArr[idx])
        joltage += int(currJoltage)
    return joltage

def findStart(arr: list[int], prevIdx: int, elementsChosen: int):
    if (elementsChosen < 11):
        startOpts = arr[prevIdx + 1:(-11 + elementsChosen)]
    else:
        startOpts = arr[prevIdx + 1:]
    start = max(startOpts)
    startIdx = startOpts.index(start) + prevIdx + 1
    return startIdx

if __name__ == "__main__":
    inputReader = InputReader(3, False)
    data = inputReader.ReadInput("\n")
    print(findMaxJoltage(data))
    print(findNewMaxJoltage(data))
    