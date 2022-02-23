""" 시각문제 """


"""
Start With Big Scale
시에 3이 들어갈 때 : 3,13,23
-> xx분 xx초 모두 valid. -> 60*60-1 = 3599
분에 3이 들어갈 때 : 3분,13분,23분,33분,43분,53분 -> 59 * 6초 모두 valid.
초에 3일 들어갈 때 : 3초,13초,23초,33초,43초,53초 -> 6 case


이런거 말고!!! 
h-m-s 에서 m이랑 s를 60까지 for문 돌리고 
string찾으면 되잖아
"""

n=int(input())
cnt=0

for h in range(n+1):
  for m in range(60):
    for s in range(60):
      _time = str(h)+str(m)+str(s)
      if '3' in _time: # .contains? just use 'IN'
        cnt+=1

print(cnt)