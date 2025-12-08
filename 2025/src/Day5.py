from InputReader import InputReader

class IdRange:
    lower: int
    upper: int

    def __init__(self, lower: int, upper: int):
        self.lower = lower
        self.upper = upper
    
    def isInRange(self, Id: int) -> bool:
        if (self.lower <= Id and Id <= self.upper):
            return True
        else:
            return False

    def mergeRange(self, other: IdRange) -> bool:
        if (self.isInRange(other.lower) or self.isInRange(other.upper)):
            self.lower = min(self.lower, other.lower)
            self.upper = max(self.upper, other.upper)
            return True
        else:
            return False
    
    def __lt__(self, other: IdRange) -> bool:
        return self.lower < other.lower
    
    def __repr__(self):
        return f"{self.lower, self.upper}"


def createIngredientRanges(data: list[str]) -> list[IdRange]:
    IdRanges = []
    for r in data:
        low, high = [int(Id) for Id in r.split("-")]
        IdRanges.append(IdRange(low, high))
    IdRanges.sort()
    return IdRanges

def mergeIdRanges(IdRanges: list[IdRange]) -> list[IdRange]:
    i = 1
    while i < len(IdRanges):
        if (IdRanges[i-1].mergeRange(IdRanges[i])):
            IdRanges.pop(i)
        else:
            i += 1
    return IdRanges

def freshItemCount(checkIds: list[str], notSpoiled: list[IdRange]) -> int:
    freshItems = 0
    for Id in checkIds:
        for r in notSpoiled:
            if (r.isInRange(int(Id))):
                freshItems += 1
                break
    return freshItems

def findFreshItems(rangeData: list[str], checkIds: list[str]) -> int:
    notSpoiled = createIngredientRanges(rangeData)
    mergedIdRange = mergeIdRanges(notSpoiled)
    freshItems = freshItemCount(checkIds, mergedIdRange)
    print("Fresh IDs: ", findFreshIds(mergedIdRange))
    return freshItems

def findFreshIds(freshIds: list[IdRange]) -> int:
    countF = 0
    for r in freshIds:
        countF += r.upper - r.lower + 1
    return countF

if __name__ == "__main__":
    inputReader = InputReader(5, False)
    data = inputReader.ReadInput("\n")
    splitPoint = data.index("")
    rangeData = data[:splitPoint]
    checkIds = data[splitPoint + 1:]
    print(findFreshItems(rangeData, checkIds))
