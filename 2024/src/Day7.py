from InputReader import InputReader
import numpy as np
from itertools import combinations

def applyOperators(data: dict):
    acceptedSum = 0
    for k in data.keys():
        combArr = ["+", "*"]*((len(data[k])-1))
        comb = list(combinations(combArr, len(data[k])-1))
        operatorArray = []
        [operatorArray.append(operator) for operator in comb if operator not in operatorArray]
        sumArr = []
        for operatorComb in operatorArray:
            operationSum = int(data[k][0])
            for i in range(len(operatorComb)):
                if operatorComb[i] == "+":
                    operationSum += int(data[k][i+1])
                else:
                    operationSum *= int(data[k][i+1])
            sumArr.append(operationSum)
        if sumArr.count(k) > 0:
            acceptedSum += k

    return acceptedSum

if __name__ == "__main__":
    inputReader = InputReader(7, False)
    data = [row.split(" ") for row in inputReader.ReadInput("\n")]
    dataDict = {}
    for equation in data:
        dataDict[int(equation[0][:-1])] = np.array(equation[1:])
    print(applyOperators(dataDict))