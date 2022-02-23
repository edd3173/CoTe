"""
  곱하기 또는 더하기
"""


s=list(map(int,input()))
Sum=s[0]
"""
4 cases
s[i] - s[i+1]
case1: x<=1 - x<=1 -> add
case2: x<=1 - x>1 -> add
case3: x>1 - x<=1 -> add
case4: x>1 - x>1 -> mul
"""
for i in range(0,len(s)-1):
  if s[i]<=1: # Case 1,2,
    Sum+=s[i+1]
  else:
    if s[i+1]<=1: # case 3
      Sum += s[i+1]
    else: # case 4
      Sum *= s[i+1]

print(Sum)