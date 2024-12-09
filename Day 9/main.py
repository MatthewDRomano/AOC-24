file = open("D:\\AOC 24\\Day 9\\input.txt", "r")
input = file.read()

blockRep = []
fileID = -1
for i in range(0, len(input), 2):
    fileID += 1
    blockRep += ([f"{fileID}"]*int(input[i]))
    if i + 1 < len(input):
        blockRep += ["."] * int(input[i+1])

def checkSum(compressedFileSystem): #sums every fileNum multiplied by its index in the file system
    checkSum, fileIDNum = 0, 0
    for n in range(len(compressedFileSystem)):
        if compressedFileSystem[n] != ".":
            checkSum += fileIDNum * int(compressedFileSystem[n])
        fileIDNum += 1
    return checkSum

def compressIndividualFiles(arr): #Compresses individual files right to left, replacing "." left to right
    l, r = 0, len(arr)-1
    while l <= r:
        while arr[l] != '.':
            l += 1
        while arr[r] == ".":
            r -= 1
        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]

    return checkSum(arr)

def compressFileBlocks(arr, ID): #Compresses entire file blocks by ID (right to left by replacing blocks of "." left to right)
    while ID >= 0:
        startIndex = arr.index(str(ID))
        endIndex = -arr[::-1].index(str(ID))
        if endIndex == 0:
            endIndex = len(arr)
            
        fileBlock = arr[startIndex:endIndex]

        for i in range(startIndex):
            if arr[i:i+len(fileBlock)] == ["."]*len(fileBlock):
                arr[i:i+len(fileBlock)], arr[startIndex:endIndex] = arr[startIndex:endIndex], arr[i:i+len(fileBlock)]
                break
        ID -= 1
    
    return checkSum(arr)

print(f"Part One: {compressIndividualFiles(blockRep.copy())}") #6607511583593
print(f"Part Two: {compressFileBlocks(blockRep.copy(), fileID)}") #6636608781232