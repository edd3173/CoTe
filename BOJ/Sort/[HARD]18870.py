"""
HARD!
"""


import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr)))
myDict = { arr2[i]: i for i in range(len(arr2))}

# print("arr1:",arr)
# print("arr2:",arr2)
# print("myDict:",myDict)

for i in arr:
    print(myDict[i],end=' ')