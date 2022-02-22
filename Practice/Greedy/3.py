"""

Q-03 : 문자열 뒤집기

0/1/0/1
0010
0000
11/0/1/000/1/000/1

divide string with chunk of 1 and 0, find the smaller number of chunk

"""
s=input()
chunk_cnt_zero=0
chunk_cnt_one=0

if s[0]=='0': chunk_cnt_zero=1
else: chunk_cnt_one=1

for i in range(0,len(s)-1):
  if s[i] != s[i+1]:
    if s[i]=='0' and s[i+1]=='1':
      chunk_cnt_one+=1
    elif s[i]=='1' and s[i+1]=='0':
      chunk_cnt_zero+=1

#print("0s : ",chunk_cnt_zero)
#print("1s : ",chunk_cnt_one)

ans=min(chunk_cnt_one,chunk_cnt_zero)
print(ans)
