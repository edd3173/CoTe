"""
떡볶이 떡 만들기
"""

n,m=list(map(int,input().split()))

arr=list(map(int,input().split()))

start=0
end=max(arr)
H=[]
ans=0

while start <= end: # Important! 결국 start와 end의 gap은 줄어든다!!!!
  sum=0
  mid = (start + end) // 2
  for x in arr:
    if x>mid:
      sum+=(x-mid)
    #else: Don't need? 문제를 읽자! 아예 떡을 얻어갈 수 없음.
     # sum+=x

   # Be Aware Of Scope!  
  if sum < m:
    end=mid-1
  else:
    H.append(mid)
    #ans=mid
    start=mid+1 


#print(H)
ans=max(H)
print(ans)
    
