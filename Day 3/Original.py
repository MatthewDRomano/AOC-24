###Lambda-Ized for shits and giggs
from functools import reduce

file = open("D:\\AOC 24\\Day 3\\input.txt", "r") 
input = file.read()

def isValidMul(mulExpr):
    if mulExpr[0] != '(' or mulExpr.count('(') != 1:
        return False
    elif mulExpr[-1] != ')' or mulExpr.count(')') != 1:
        return False
    
    elif ',' not in mulExpr or mulExpr.count(',') != 1:
        return False
    
    return reduce(lambda x, y : x and y, map(lambda char : char in 'mul(),0123456789', mulExpr))

subInput = input
for i in range(2):
    temp = [expr for expr in [element.split(')')[0] + ')' for element in subInput.split("mul")] if isValidMul(expr)]
    total = reduce(lambda a, b : a + b, [reduce(lambda x, y : int(x)*int(y), (pair[1:-1].split(','))) for pair in temp])
    print(f"Part {i+1}: {total}")
    subInput = "".join([term.split("don't()")[0] for term in input.split("do()")])
#subInput: split by do(), perform every valid mul (left to right) until a don't appears in the splitted parts 
#reduce = lambda fn, obj : [fn(obj[i], obj[i+1]) for i in range(len(obj)-1)]