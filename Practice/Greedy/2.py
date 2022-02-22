"""
Q-02 : 곱하기 혹은 더하기
"""
s=list(input())
#print(s)
ans=int(s[0])

for i in range(1,len(s)):
  data=int(s[i])
  if ans <=1 or data <=1 : # ans must be cascaded, else problem
    ans += data # Like an example '10203'.
  else:
    ans *= data    

print(ans)