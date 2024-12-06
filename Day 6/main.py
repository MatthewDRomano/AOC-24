file = open("D:\AOC 24\Day 6\input.txt", "r")
matrix = [list(line.strip()) for line in file.readlines()]


for i in range(len(matrix)):
    if "^" in matrix[i]:
        STARTPOSITION = ((i, matrix[i].index("^")), "North")
        break

#STARTPOSITION = [((i, matrix[i].index("^")), "North") for i in range(len(matrix)) if "^" in matrix[i]][0]
pos = STARTPOSITION
positionsVisited = [pos]


def inMatrix(pos):
    if pos[0][0] < 0 or pos[0][0] >= len(matrix):
        return False
    if pos[0][1] < 0 or pos[0][1] >= len(matrix[0]):
        return False
    return True

def rotate(direction):
    directionMap = ["North", "East", "South", "West", "North"]
    return directionMap[directionMap.index(direction)+1]

def move(curPosition):
    if curPosition[1] == "North":
        return ((curPosition[0][0]-1, curPosition[0][1]), curPosition[1])
    elif curPosition[1] == "East":
        return ((curPosition[0][0], curPosition[0][1]+1), curPosition[1])
    elif curPosition[1] == "South":
        return ((curPosition[0][0]+1, curPosition[0][1]), curPosition[1])
    elif curPosition[1] == "West":
        return ((curPosition[0][0], curPosition[0][1]-1), curPosition[1])
    

while inMatrix(pos):
    projectedPosition = move(pos)
    
    if inMatrix(projectedPosition):
        if matrix[projectedPosition[0][0]][projectedPosition[0][1]] == "#":
            pos = ((pos[0][0], pos[0][1]), rotate(pos[1]))
            continue
    else:
        break

    pos = projectedPosition
    if matrix[pos[0][0]][pos[0][1]] == ".":
        matrix[pos[0][0]][pos[0][1]] = "X"
        positionsVisited += [pos]


print(f"Part One: {len(positionsVisited)}")


amtSpots = 0
for position in positionsVisited:
    if position == STARTPOSITION:
        continue
        
    matrix[position[0][0]][position[0][1]] = "#"
    pos = STARTPOSITION
    rotationLocations = []

    while inMatrix(pos):
        projectedPosition = move(pos)

        if inMatrix(projectedPosition):
            if matrix[projectedPosition[0][0]][projectedPosition[0][1]] == "#":
                pos = ((pos[0][0], pos[0][1]), rotate(pos[1]))
                rotationLocations += [pos]
 
                if rotationLocations.count(pos) > 2:
                    amtSpots += 1
                    break

            else:
                pos = projectedPosition
        else:
            break

    matrix[position[0][0]][position[0][1]] = "."

print(f"Part Two: {amtSpots}")