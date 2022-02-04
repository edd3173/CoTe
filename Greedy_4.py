
''' 공포도문제 '''

n=int(input())
data=list(map(int,input().split()))
data.sort()

ans=0
gm=0

'''
n=5
d=1,2,2,2,3
'''

for idx in range(0,len(data)):
  cf=data[idx] #Current Fear
  gm+=1 #Current group member

  #Check if gm >= cf
  if(gm >= cf):
    ans+=1 #Update ans
    gm=0 #Initialize Group


print(ans)