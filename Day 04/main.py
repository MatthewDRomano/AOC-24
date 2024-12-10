file = open("D:\AOC 24\Day 4\input.txt", "r")
input = file.read()

matrix = [list(line) for line in input.split("\n")]

def east(r, c):
    if c + 3 >= len(matrix[r]):
        return 0

    word = matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] + matrix[r][c+3]
    return 1 if word == "XMAS" or word == "SAMX" else 0

def south(r, c):
    if r + 3 >= len(matrix):
        return 0

    word = matrix[r][c] + matrix[r+1][c] + matrix[r+2][c] + matrix[r+3][c]
    return 1 if word == "XMAS" or word == "SAMX" else 0

def southEast(r, c):
    if c + 3 >= len(matrix[r]) or r + 3 >= len(matrix):
        return 0
    
    word = matrix[r][c] + matrix[r+1][c+1] + matrix[r+2][c+2] + matrix[r+3][c+3]
    return 1 if word == "XMAS" or word == "SAMX" else 0

def northEast(r, c):
    if c + 3 >= len(matrix[r]) or r - 3 < 0:
        return 0
    
    word = matrix[r][c] + matrix[r-1][c+1] + matrix[r-2][c+2] + matrix[r-3][c+3]
    return 1 if word == "XMAS" or word == "SAMX" else 0


def isX_MAS(r, c):
    if r == 0 or c == 0 or r + 1 == len(matrix) or c + 1 == len(matrix[r]):
        return 0
    
    word1 = matrix[r-1][c-1] + matrix[r][c] + matrix[r+1][c+1]
    word2 = matrix[r-1][c+1] + matrix[r][c] + matrix[r+1][c-1]
    return 1 if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM") else 0

partOneTotal, partTwoTotal = 0, 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        partOneTotal += east(i, j)
        partOneTotal += south(i, j)
        partOneTotal += southEast(i, j)
        partOneTotal += northEast(i, j)

        partTwoTotal += isX_MAS(i, j)

print(f"Part One: {partOneTotal}")
print(f"Part Two: {partTwoTotal}")