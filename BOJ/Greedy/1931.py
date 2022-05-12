N=int(input())
data=[]
for _ in range(N):
    x,y = map(int,input().split())
    z = y - x
    data.append((x,y))

data.sort(key=lambda x:(x[1],x[0]))
#print(data)

"""
같은 시작점 : 끝점이 작을수록 무조건 유리.
다른 시작점?

"""
last=0; ans=0
for x,y in data:
    if x>=last:
        last=y
        ans+=1
        
print(ans)