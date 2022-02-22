arr=[i*i for i in range(1,10)]
print(arr)

n=3; m=4
arr=[[0]*m for _ in range(n)]

a=[1,2,3,4,5,5,5]
remove_set={3,5}

a= [i for i in a if i not in remove_set]

def add(a,b):
    return a+b

print((lambda a,b: a+b)(3,5))

#import sys
#data=sys.stdin.readline().rstrip()
#print(data)

data= [('a',15),('b',30),('c',10),('d',5)]

data=sorted(data, key = lambda x:x[1],reverse=True)

print(data)

from itertools import permutations
data=['a','b','c']
result=list(permutations(data,3))
print(result)

from itertools import product

data=['a','b','c']
result=list(product(data,repeat=2))
print(result)

from bisect import bisect_left, bisect_right

a=[1,2,4,4,8]
left=bisect_left(a,4)
right=bisect_right(a,4)
print(left,right)
