file = open("D:\AOC 24\Day 10\\input.txt", "r")
topograhicMap = [list(line.strip()) for line in file.readlines()]

trailHeadPositions = []
for r in range(len(topograhicMap)): #adds all trail head (0s) positions
    for c in range(len(topograhicMap[r])):
        if topograhicMap[r][c] == "0":
            trailHeadPositions += [(r, c)]


def dfs(pos, peaksVisited, value = 0):
    if value == 9: # if peak is reached
        if "SCORE" in peaksVisited: #only adds to visited array if checking for 'Score" (Explanation: SEE LINEs 31-32)
            peaksVisited += [pos]
        return 1
    
    left, right, down, up = 0, 0, 0, 0
    if pos[0] > 0 and int(topograhicMap[pos[0]-1][pos[1]]) == value+1 and (pos[0]-1, pos[1]) not in peaksVisited: #up
        up = dfs((pos[0]-1, pos[1]), peaksVisited, value+1)
    if pos[0] + 1 < len(topograhicMap) and int(topograhicMap[pos[0]+1][pos[1]]) == value+1 and (pos[0]+1, pos[1]) not in peaksVisited: #down
        down = dfs((pos[0]+1, pos[1]), peaksVisited, value+1)
    if pos[1] > 0 and int(topograhicMap[pos[0]][pos[1]-1]) == value+1 and (pos[0], pos[1]-1) not in peaksVisited: #left
        left = dfs((pos[0], pos[1]-1), peaksVisited, value+1)
    if pos[1] + 1 < len(topograhicMap[0]) and int(topograhicMap[pos[0]][pos[1]+1]) == value+1 and (pos[0], pos[1]+1) not in peaksVisited: #right
        right = dfs((pos[0], pos[1]+1), peaksVisited, value+1)

    return up + down + left + right

totalScores, totalRanges = 0, 0
for trailhead in trailHeadPositions:
    totalScores += dfs(trailhead, ["SCORE"]) # Score -> Number of peaks (9) every trailhead (0) can reach via dfs
    totalRanges += dfs(trailhead, ["RATING"]) # Rating -> Number of paths every trailhead (0) has to a peak(9) via dfs

print(f"Part One: {totalScores}") # 638
print(f"Part Two: {totalRanges}") # 1289