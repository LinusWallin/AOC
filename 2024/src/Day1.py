from InputReader import InputReader
import numpy as np


def splitData(data):
    return (np.array([row.split("   ") for row in data])).astype(int)


def sortCols(data):
    # data = data.astype(int)
    data = np.sort(data, axis=0)
    return data


def diffSum(matrix):
    diff = abs(np.subtract(matrix[:, 0], matrix[:, 1]))
    return sum(diff)


def occurances(data, num):
    occ = 0
    for i in range(len(data)):
        if data[i, 1] == num:
            occ += 1
        elif data[i, 1] > num:
            break
    return occ


def calcOccSum(data):
    s = 0
    for num in data[:, 0]:
        s += num * occurances(data, num)
    return s


if __name__ == "__main__":
    inputReader = InputReader(1, False)
    data = inputReader.ReadInput("\n")
    dataMat = splitData(data)
    sortedData = sortCols(dataMat)
    print(diffSum(sortedData))
    print(calcOccSum(sortedData))
