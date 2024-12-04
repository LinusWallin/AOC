from InputReader import InputReader


def charDir(
    data: list[list[str]], idx: list[int], dir: list[int], word: str, char: int
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


def findChar(data: list[list[str]], idx: list[int], word: str, char: int):
    found = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            found += charDir(data, idx, [i, j], word, char)
    return found


def findWordOcc(data: list[list[str]], word: str):
    words = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == word[0]:
                words += findChar(data, [i, j], word, 1)
    return words


if __name__ == "__main__":
    inputReader = InputReader(4, False)
    data = inputReader.ReadInput("\n")
    data = [list(row) for row in data]
    print(findWordOcc(data, "XMAS"))
