from InputReader import InputReader

def findInvalidId(data:list[str], s:bool) -> int:
    total = 0
    for IdRange in data:
        r = IdRange.split("-")
        start = int(r[0])
        end = int(r[1]) + 1
        for num in range(start, end):
            if (checkForCopies(num)):
                total += num
            elif (checkRepetitions(num) and s):
                total += num
    return total

def checkForCopies(num:int) -> bool:
    numString = str(num)
    if (len(numString) % 2 == 0):
        s1 = numString[:len(numString)//2]
        s2 = numString[len(numString)//2:]
        if (s1 == s2):
            return True
        else:
            return False

def checkRepetitions(num:int) -> bool:
    numString = str(num)
    l = len(numString)
    for x in range(1, l//2 + 1):
        if (l%x == 0):
            copy = numString[:x] * (l//x)
            if (copy == numString):
                return True
    return False

if __name__ == "__main__":
    inputReader = InputReader(2, False)
    data = inputReader.ReadInput(",")
    print(findInvalidId(data, True))
    