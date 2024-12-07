file = open("D:\AOC 24\Day 7\input.txt", "r")
parts = [line.split(":") for line in file.readlines()]
testValues = [int(part[0]) for part in parts]
nums = [part[1].strip().split(" ") for part in parts]

add = lambda x, y : x + y
multiply = lambda x, y : x * y
concatinate = lambda x, y : int(str(x) + str(y))
#Implemented functions

def solveEquation(numArr, base_N_OperationStr, operations): # applies base_N operation string to numArr // returns total
    answer = int(numArr[0])
    index = 1

    for digit in base_N_OperationStr:
        answer = operations[int(digit)](answer, int(numArr[index]))
        index += 1
    return answer

def decimalToBaseN(decimalNum, base): #allows up to base 36
    if decimalNum == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    result = ""

    while decimalNum > 0:
        remainder = decimalNum % base
        result = digits[remainder] + result
        decimalNum //= base

    return result

def increment(base_N_OperationStr, base): # increments the operation representation string based on the given base
    decimalForm = 0
    power = 0
    for digit in base_N_OperationStr[::-1]:
        decimalForm += (int(digit) * (base**power))
        power += 1
    decimalForm += 1

    base_N_Form = decimalToBaseN(decimalForm, base)
    return "0"*(len(base_N_OperationStr)-len(base_N_Form)) + base_N_Form
    
def findCalibrationTotal(operations):
    totalCalibrationResults = 0
    for i in range(len(nums)):
        answer = 0
        base_N_OperationRepresentation = "0"*(len(nums[i])-1) # 0 - n // n representing base n+1

        while True:
            answer = solveEquation(nums[i], base_N_OperationRepresentation, operations)

            if answer == testValues[i]:
                totalCalibrationResults += testValues[i]
                break
            elif base_N_OperationRepresentation == f"{len(operations)-1}"*(len(nums[i])-1):
                break

            base_N_OperationRepresentation = increment(base_N_OperationRepresentation, len(operations))
    return totalCalibrationResults
    
print(findCalibrationTotal([add, multiply])) # list of operations
print(findCalibrationTotal([add, multiply, concatinate])) # list of operations