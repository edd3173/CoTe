"""
정수 삼각형
"""

n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
    
#print(arr)

for i in range(1,n):
    for j in range(0,i+1):
        if j==0:
            arr[i][j]=arr[i-1][0]+arr[i][j]
        elif j==i:
            arr[i][j]=arr[i-1][i-1]+arr[i][j]
        else:
            arr[i][j]=max(arr[i-1][j-1]+arr[i][j],arr[i-1][j]+arr[i][j]) 

print(max(arr[n-1]))