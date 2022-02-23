n,m = map(int,input().split())
datas=list(map(int,input().split()))
datas.sort()
ans=[]

def getVal(arr, height):
  sum=0
  for data in arr:
    if data<height:
      continue
    elif data>=height:
      sum+=data-height
  return sum

def binary_search(target,start,end): # array안의 data를 찾는게 아니잖아?
  global datas
  while start<=end:
    mid = (start+end) // 2
    val = getVal(datas,mid)
    if val < target:
      end=mid-1
    elif val >= target: # 떡길이>타겟. 따라서 start를 올려야. end를 줄이는 것이 아니다!! end를 줄이면 떡 양이 늘어나지.
      ans.append(mid)
      start=mid+1

binary_search(m, 0, max(datas))
print(max(ans))



"""
Point1. arr 안의 값을 찾는 것이 아니다! 더 단순함! 하지만 더 어렵다
Point2. 일반적인 이진탐색 코드와 반대. 이 문제에서는 end를 줄이면 떡양이 늘어남. 따라서 start를 늘려서 떡양을 줄여야.
자 크기에 꼳히지 말고, 떡 양에 집중

"""