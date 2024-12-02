import functools

file = open("D:\AOC 24\Day 1\input.txt", "r")
lines = file.readlines()

sum = lambda x, y : x + y

### PART ONE 
left = sorted([(int)(line.split("   ")[0]) for line in lines])
right = sorted([(int)(line.split("   ")[1]) for line in lines])

print(functools.reduce(sum, map(lambda l, r : abs(r-l), left, right)))

### PART TWO
print(functools.reduce(sum, map(lambda l : right.count(l)*l, left)))