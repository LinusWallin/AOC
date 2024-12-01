from InputReader import InputReader
import numpy as np

def splitData(data):
    return np.array([row.split("   ") for row in data])

def sortCols(data):
    data = data.astype(int)
    data = np.sort(data, axis=0)
    return data

def diffSum(matrix):
    diff = abs(np.subtract(matrix[:,0], matrix[:,1]))
    return sum(diff)

if __name__ == "__main__":
    inputReader = InputReader(1, False)
    data = inputReader.ReadInput("\n")
    dataMat = splitData(data)
    sortedData = sortCols(dataMat)
    print(diffSum(sortedData))
    

