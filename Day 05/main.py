file = open("D:\AOC 24\Day 5\input.txt", "r")
page_Ordering_Rules, pages = [part.split("\n") for part in (file.read()).split("\n\n")]

correctlyOrderedSum, inCorrectlyOrderedSum = 0, 0

def getCorrectedPage(map, pageNums, rules):
    correctPage = []
    addAtEnd = []
    mapIndex = 0
    for num in pageNums:
        if num in map.keys():
            correctPage += [int(list(map.keys())[mapIndex])]
            mapIndex += 1
        elif num in [rule.split("|")[1] for rule in rules]:
            addAtEnd += [num]
        else:
            correctPage += [int(pageNums[pageNums.index(num)])]
    correctPage += addAtEnd

    return correctPage
        


for page in pages:
    isValid = True
    numsInPage = page.split(",")
    
    before_Map = {} # KEYS: numbers appearing in left side of rules VALUES: amount of numbers they must be before in given page
    for rule in page_Ordering_Rules:
        before, after = rule.split("|")
        
        if before in numsInPage and after in numsInPage:
            if (numsInPage.index(before) > numsInPage.index(after)):
                isValid = False

            before_Map[before] = before_Map[before] + 1 if before in before_Map else 1

    before_Map = {k: v for k, v in sorted(before_Map.items(), key=lambda item: item[1], reverse=True)} #sorted by increasing values
    correctPage = getCorrectedPage(before_Map, numsInPage, page_Ordering_Rules)

    if isValid:
        correctlyOrderedSum += int(numsInPage[len(numsInPage)//2])
    else:
        inCorrectlyOrderedSum += int(correctPage[len(correctPage)//2])

print(f"Part One: {correctlyOrderedSum}")
print(f"Part Two: {inCorrectlyOrderedSum}")