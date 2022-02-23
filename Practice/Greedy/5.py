"""
Q-05 : 볼링공 고르기
"""

n,m = map(int,input().split())
data=list(map(int,input().split()))
res=0

"""
# Using Combination
# nC2 니까 n^2. n<=1000이니까 적법한거같은데?

from itertools import combinations

c_list = combinations(data,2)
for list in c_list:
    if list[0]==list[1]:
        pass
    else:
        cnt+=1
        
print(cnt)
"""

arr = [0] * 11
for x in data:
    arr[x]+=1
print(arr)

"""
for i in range(1,m+1):
    n-=arr[i]
    res+=arr[i]*n

print(res)
"""