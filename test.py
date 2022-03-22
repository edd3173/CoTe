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
    cur = weights[i] * sum(weights[i+1::])
    #print(cur)
    ans+=cur
print(ans)