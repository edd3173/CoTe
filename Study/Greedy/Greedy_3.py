"""
  곱하기 또는 더하기
"""



"""
4 cases
s[i] , s[i+1]
case1: x<=1 , x<=1 -> add
case2: x<=1 , x>1 -> add
case3: x>1 , x<=1 -> add
case4: x>1 , x>1 -> mul


data=input()
result=int(data[0])

for i in range(1,len(data)):
    num = int(data[i])
    if num<=1 or result<=1:
        result += num
    else:
        result *= num
        
print(result)

"""


data = input()

numArr = [int(i) for i in data]
#print(numArr)
ans=numArr[0]

"""
조건문 주의! 
두 숫자가 모두 1보다 작거나 같은걸 따지는 건 맞는데.
하나는 arr[i+1]이고, 다른 하나는 arr[i]가 아니라, 지금까지 계산한 값이다!
그렇지 않다면 24015는 에러남
2x4+1x5 가 아니라, 2x4+1+5가 되버림
"""


for i in range(0,len(numArr)-1):
  if ans <=1 or numArr[i+1]<=1:
    ans += numArr[i+1]
  else:
    ans *= numArr[i+1]

print(ans)

