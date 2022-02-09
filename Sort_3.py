"""
위에서 아래로
"""

n = int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

print(arr)
