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

n,m = map(int,input().split())
arr = list(map(int,input().split()))
weights =[0] * 10

for data in arr:
    weights[data] += 1
"""
1 - 1
2 - 2
3 - 2

1 * (2+2)
+
2 * 2


1 - 1
2 - 2
3 - 1
4 - 2
5 - 2

1 * (2+1+2+2)
+
2 * (1+2+2)
+
1 * (2+2)
+
2 * 2

7+10+4+4 = 25


"""

#Iterate through weights
#print(weights)
ans=0
for i in range(1,m+1):
    cur = weights[i] * sum(weights[i+1:])
    #print(cur)
    ans+=cur
print(ans)