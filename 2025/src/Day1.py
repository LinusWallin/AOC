from InputReader import InputReader

def findPassword(data:list[str], currRot:int, new:bool) -> int:
    password = 0
    for rot in data:
        steps = int(rot[1:])
        if rot[0] == "L":
            if new:
                if currRot <= steps:
                    if currRot != 0:
                        password += 1
                    steps -= currRot
                    currRot = 0
                    password += steps // 100
            currRot -= steps
        else:
            if new:
                if 100 - currRot <= steps:
                    password += 1
                    steps -= 100 - currRot
                    currRot = 100
                    password += steps // 100
            currRot += steps
        currRot %= 100
        if currRot == 0 and not new:
            password += 1
    return password

if __name__ == "__main__":
    inputReader = InputReader(1, False)
    data = inputReader.ReadInput("\n")
    startRot = 50
    password = findPassword(data, startRot, True)
    print(password)
