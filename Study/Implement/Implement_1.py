""" 상하좌우 """

dx=[1,-1,0,0]
dy=[0,0,-1,1]
#moves=['D','U','L','R']

px=1
py=1

n=int(input())
data=list(input().split())

print(n)
print(data)

for action in data:
  if(action == 'R'):
    nx=px+dx[3]; ny=py+dy[3]
  elif(action == 'L'):
    nx=px+dx[2]; ny=py+dy[2]
  elif(action == 'U'):
    nx=px+dx[1]; ny=py+dy[1]
  elif(action == 'D'):
    nx=px+dx[0]; ny=py+dy[0]

  if(nx<1 or nx>n or  ny<1 or ny>n): #number 'n'!!!
    continue # Do Nothing
  else:
    px=nx; py=ny; #Update 
    

print(px,py)

