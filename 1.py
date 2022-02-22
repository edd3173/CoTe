"""
Q-01 : 모험가길드
"""



N = int(input())
arr = list(map(int,input().split()))
arr.sort()
group_num=0; member_num=0

"""
2 3 1 2 2 3
1 2 2 2 3 3
*   *    
"""


for i in range(0,len(arr)):
  member_num+=1
  cur=arr[i]
  if member_num >= arr[i]:
    group_num+=1
    member_num=0

print(group_num)