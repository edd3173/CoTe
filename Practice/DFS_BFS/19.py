"""
연산자 끼워넣기
"""

from itertools import permutations

n = int(input())
Operands = [0,0,0,0]
numbers = list(map(int,input().split()))
opers = list(map(int,input().split()))
for i in range(4):
    Operands[i] = opers[i]


# Operand list
OperString = []
for _ in range(Operands[0]):
    OperString.append('+')
for _ in range(Operands[1]):
    OperString.append('-')
for _ in range(Operands[2]):
    OperString.append('*')
for _ in range(Operands[3]):
    OperString.append('/')
#print(OperString)
# we can use permutation
PossibleStrings = permutations(OperString, len(OperString))
#print(PossibleStrings)
# values
MIN = int(1e9)
MAX = -MIN

# for possible cases, calc/update values
for currentString in PossibleStrings:
    #print(currentString)
    
    curVal = numbers[0]
    #MIN=curVal; MAX=curVal
    for i in range(n-1):
        if currentString[i] == '+':
            curVal += numbers[i+1]
        elif currentString[i] == '-':
            curVal -= numbers[i+1]
        elif currentString[i] == '*':
            curVal *= numbers[i+1]
        elif currentString[i] == '/':
            curVal = int(curVal / numbers[i+1])
            
    #print("evalVal :",curVal)    
    # max,min for currentString eval
    MAX = max(MAX,curVal)
    MIN = min(MIN,curVal)
    #print("CurrentString's max and min : ",MAX,MIN)
    
print(MAX)
print(MIN)
            