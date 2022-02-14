"""
  모험가 길드
"""


n=int(input())
arr=list(map(int,input().split()))
arr.sort()

#print(arr)

group_num=0
member_num=1

for idx in range(n):
  member_num+=1 # 비교하기 전에 우선 그룹에 넣는다.
  if member_num >= arr[idx]: # 멤버수 >= 공포도
    member_num=0
    group_num+=1
  
print(group_num)