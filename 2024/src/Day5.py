from InputReader import InputReader

def splitInput(data: list[str]):
    rules = {}
    updates = []
    for row in data:
        if row.__contains__("|"):
            rule = row.split("|")
            try:
                if rules[rule[0]] != None:
                    rules[rule[0]].append(rule[1])
            except:
                rules[rule[0]] = [rule[1]]
        else:
            if row == "":
                continue
            else:
                updates.append(row.split(","))
    return rules, updates

def validateUpdate(rules: dict, update: list[str]):
    for i, num in enumerate(update):
        try:
            keyArr = [k for k in rules.keys() if num in rules[k]]
            for prioNum in keyArr:
                if prioNum in update:
                    prioIdx = update.index(prioNum)
                    if prioIdx < i:
                        continue
                    else:
                        return False
        except:
            print("Error", i)
            return False
    return True

def pageNumSum(rules:dict , updates: list[list[str]]):
    numSum = 0
    for update in updates:
        if validateUpdate(rules, update):
            centralUpdate = len(update)//2
            numSum += int(update[centralUpdate])
    return numSum


if __name__ == "__main__":
    inputReader = InputReader(5, False)
    data = inputReader.ReadInput("\n")
    rules, updates = splitInput(data)
    print(pageNumSum(rules, updates))
    