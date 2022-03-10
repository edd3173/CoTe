"""
  모험가 길드
"""


n=int(input())
data = list(map(int,input().split()))

data.sort()

groupNum=0
memberNum=0

"""
1 2 2 2 3
"""
for i in range(0,len(data)):
  
  cur=data[i]
  memberNum+=1
  
  if memberNum >= cur:
    groupNum += 1
    memberNum = 0

print(groupNum)
    