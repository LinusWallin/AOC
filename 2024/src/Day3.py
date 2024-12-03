from InputReader import InputReader
import numpy as np


def getMulSum(data: list[str]):
    mulSum = 0
    do = True
    for i, char in enumerate(data):
        if char == "m" and do:
            mulStr = "".join(data[i : i + 4])
            if mulStr == "mul(":
                idx, firstNum = number(data, i + 4)
                if data[idx] == ",":
                    idx, secondNum = number(data, idx + 1)
                    if data[idx] == ")":
                        mulSum += firstNum * secondNum
        elif char == "d":
            if "".join(data[i : i + 4]) == "do()":
                do = True
            elif "".join(data[i : i + 7]) == "don't()":
                do = False
    return mulSum


def number(data: list[str], index: int):
    num = ""
    while data[index].isdigit():
        num += data[index]
        index += 1
    return index, int(num)


if __name__ == "__main__":
    inputReader = InputReader(3, False)
    data = inputReader.ReadInput("\n")
    corrupetInput = list(data[0])
    for i in range(1, len(data)):
        corrupetInput = np.concatenate((corrupetInput, list(data[i])))
    print(getMulSum(corrupetInput))
