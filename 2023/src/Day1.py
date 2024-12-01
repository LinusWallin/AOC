from InputReader import InputReader
import os

def findNumbers(row):
    left = ""
    right = ""
    for char in row:
        if char.isdigit():
            if left == "":
                left = char
                right = char
            else:
                right = char
    return left + right

def calcSum(vals):
    return sum([int(val) for val in vals])


if __name__ == "__main__":
    inputReader = InputReader(1, False)
    data = inputReader.ReadInput("\n")
    print(calcSum(findNumbers(row) for row in data))
