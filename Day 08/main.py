file = open("D:\AOC 24\Day 8\input.txt", "r")
matrix = [list(line.strip()) for line in file.readlines()]


def inMatrix(locationTuple): # checks if location is in bounds of 2D matrix
    if locationTuple[0] < 0 or locationTuple[0] >= len(matrix):
        return False
    if locationTuple[1] < 0 or locationTuple[1] >= len(matrix[0]):
        return False
    return True

antennaLocations = {} # KEYS: antenna (denoted by digit or letter) VALUES: List of positions that frequency occurs 

for r in range(len(matrix)): # fills antennaLocations 
    for c in range(len(matrix[r])):
        if matrix[r][c] == ".":
            continue
        if matrix[r][c] not in antennaLocations:
            antennaLocations[matrix[r][c]] = [(r, c)]
        else:
            antennaLocations[matrix[r][c]] += [(r, c)]

uniqueAntiNodeLocationsPartOne, uniqueAntiNodeLocationsPartTwo = [], []

for frequency in antennaLocations:
    for i in range(len(antennaLocations[frequency])):

        if len(antennaLocations[frequency]) > 1:
            uniqueAntiNodeLocationsPartTwo += [location for location in antennaLocations[frequency] if location not in uniqueAntiNodeLocationsPartTwo]

        for j in range(i+1, len(antennaLocations[frequency])):
            antennaOffset = (antennaLocations[frequency][i][0] - antennaLocations[frequency][j][0], antennaLocations[frequency][i][1] - antennaLocations[frequency][j][1])
            antennaOffsetInverse = (-antennaOffset[0], -antennaOffset[1])

            antiNodeLocationOne = (antennaLocations[frequency][i][0] + antennaOffset[0], antennaLocations[frequency][i][1] + antennaOffset[1])
            antiNodeLocationTwo = (antennaLocations[frequency][j][0] + antennaOffsetInverse[0], antennaLocations[frequency][j][1] + antennaOffsetInverse[1])


            if inMatrix(antiNodeLocationOne) and antiNodeLocationOne not in uniqueAntiNodeLocationsPartOne:
                uniqueAntiNodeLocationsPartOne += [antiNodeLocationOne]
            if inMatrix(antiNodeLocationTwo) and antiNodeLocationTwo not in uniqueAntiNodeLocationsPartOne:  
                uniqueAntiNodeLocationsPartOne += [antiNodeLocationTwo]
            ###Part One Conditonals Above

            while inMatrix(antiNodeLocationOne):
                if antiNodeLocationOne not in uniqueAntiNodeLocationsPartTwo:
                    uniqueAntiNodeLocationsPartTwo += [antiNodeLocationOne]
                antiNodeLocationOne = (antiNodeLocationOne[0] + antennaOffset[0], antiNodeLocationOne[1] + antennaOffset[1])

            while inMatrix(antiNodeLocationTwo):
                if antiNodeLocationTwo not in uniqueAntiNodeLocationsPartTwo:
                    uniqueAntiNodeLocationsPartTwo += [antiNodeLocationTwo]
                antiNodeLocationTwo = (antiNodeLocationTwo[0] + antennaOffsetInverse[0], antiNodeLocationTwo[1] + antennaOffsetInverse[1])
            ###Part Two Loops/Conditonals Above
                
print(f"Part One: {len(uniqueAntiNodeLocationsPartOne)}") # 249
print(f"Part Two: {len(uniqueAntiNodeLocationsPartTwo)}") # 905