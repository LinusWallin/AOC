from InputReader import InputReader
import numpy as np


def charDir(
    data: list[list[str]],
    idx: list[int],
    dir: list[int],
    word: str,
    char: int,
):
    found = 0
    if char > len(word) - 1:
        return 1
    idx = [idx[i] + dir[i] for i in range(2)]
    if idx[0] < 0 or idx[0] > len(data) - 1 or idx[1] < 0 or idx[1] > len(data[0]) - 1:
        return 0
    if data[idx[0]][idx[1]] == word[char]:
        found = charDir(data, idx, dir, word, char + 1)
    return found


def findChar(
    data: list[list[str]],
    idx: list[int],
    word: str,
    char: int,
):
    found = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            found += charDir(data, idx, [i, j], word, char)
    return found


def findXShape(data, idx: list[int], word: str):
    for comb in range(4):
        if comb % 2 == 0:
            tL = 0
            bR = 2
        else:
            tL = 2
            bR = 0

        if comb > 0 and comb < 3:
            tR = 0
            bL = 2
        else:
            tR = 2
            bL = 0

        if idx[0] > data.shape[0] - 3 or idx[1] > data.shape[1] - 3:
            return 0

        wordMat = np.array(
            [
                [word[tL], data[idx[0], idx[1] + 1], word[tR]],
                [data[idx[0] + 1, idx[1]], word[1], data[idx[0] + 1, idx[1] + 2]],
                [word[bL], data[idx[0] + 2, idx[1] + 1], word[bR]],
            ]
        )

        if np.all((data[idx[0] : (idx[0] + 3), idx[1] : (idx[1] + 3)]) == wordMat):
            return 1

    return 0


def findWordOcc(
    data: list[list[str]],
    word: str,
    char: str,
    xShape: bool,
):
    words = 0
    dataMat = np.array(data)
    for i in range(len(data)):
        for j in range(len(data[0])):
            charIdx = word.index(char)
            if xShape:
                words += findXShape(dataMat, [i, j], word[1:])
            elif not xShape and data[i][j] == char:
                charIdx += 1
                words += findChar(data, [i, j], word, charIdx)
    return words


if __name__ == "__main__":
    inputReader = InputReader(4, False)
    data = inputReader.ReadInput("\n")
    data = [list(row) for row in data]
    print(findWordOcc(data, "XMAS", "X", False))
    print(findWordOcc(data, "XMAS", "A", True))
