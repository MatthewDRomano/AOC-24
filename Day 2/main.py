with open("input.txt", "r") as file:
    lines = file.readlines()

def isSafe(list):
    if list != sorted(list) and list != sorted(list)[::-1]:
        return False
    
    for i in range(len(list) - 1):
        if abs(list[i] - list[i + 1]) < 1 or abs(list[i] - list[i + 1]) > 3:
            return False
    return True


numSafePartOne, numSafePartTwo = 0, 0
for line in lines:
    report = list(map(int, line.strip().split()))
    if isSafe(report):
        numSafePartOne += 1
        numSafePartTwo += 1
    else: 
        for i in range(len(report)):
            if isSafe(report[:i] + report[i+1:]):
                numSafePartTwo += 1
                break

    
print(f"Part One: {numSafePartOne}")
print(f"Part Two: {numSafePartTwo}")