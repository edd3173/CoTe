
n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

answers=[]

def getVal(height): # height가 늘어날수록 떡은 줄어들지.
  total=0
  for element in arr:
    if element-height>0:
      total+=element-height
  return total

def binary_search(arr,target,start,end):
  while start<=end:
    mid = (start+end) // 2
    if getVal(mid) >= target: # 적합한 조건. height를 조금 늘려도 되겠는데?
      start=mid+1 # 그럼 start를 높여서 조건만족하는 최대값을 찾아보자
      answers.append(mid) # 후보군에 넣음.
    else: # 적합하지 않네. height가 너무 크다.
      end=mid-1  # 따라서 줄어들지.
  return None

binary_search(arr, m, 0, max(arr))

print(answers)






"""
Point1. arr 안의 값을 찾는 것이 아니다! 더 단순함! 하지만 더 어렵다
Point2. 일반적인 이진탐색 코드와 반대. 이 문제에서는 end를 줄이면 떡양이 늘어남. 따라서 start를 늘려서 떡양을 줄여야.
#자 크기에 꼳히지 말고, 떡 양에 집중

"""