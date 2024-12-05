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


def validateUpdate(rules: dict, update: list[str], fix: bool):
    changed = False
    for i, num in enumerate(update):
        try:
            keyArr = [k for k in rules.keys() if num in rules[k]]
            for prioNum in keyArr:
                if prioNum in update:
                    prioIdx = update.index(prioNum)
                    if prioIdx < i:
                        continue
                    else:
                        if fix:
                            copyUpd = update.copy()
                            copyUpd[i] = update[prioIdx]
                            copyUpd[prioIdx] = update[i]
                            valid, changed, update = validateUpdate(
                                rules, copyUpd, True
                            )
                            if valid:
                                changed = True
                                return True, changed, update
                        return False, changed, update
        except:
            print("Error", i)
            return False, changed, update
    return True, changed, update


def fixUpdate(rules: dict, updates: list[list[str]]):
    return False


def pageNumSum(rules: dict, updates: list[list[str]], fix: bool):
    numSum = 0
    for update in updates:
        if fix:
            valid, updateValidataion, update = validateUpdate(rules, update, True)
        else:
            updateValidataion, _, update = validateUpdate(rules, update, False)
        if updateValidataion:
            centralUpdate = len(update) // 2
            numSum += int(update[centralUpdate])
    return numSum


if __name__ == "__main__":
    inputReader = InputReader(5, False)
    data = inputReader.ReadInput("\n")
    rules, updates = splitInput(data)
    print(pageNumSum(rules, updates, False))
    print(pageNumSum(rules, updates, True))
