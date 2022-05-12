S=input().strip()

possibles=set()

myString=""
for i in range(1,len(S)+1):
    for j in range(0,len(S)-i+1):
        # i==2일때, j는 어디까지여야 하는가?
        # i==2일때, max는 bc : S[3:5]
        # min은 ab : S[0:2]
        # j는 min 0 ~ 3까지다.
        # 여기서 3이 뭐냐? i+1이냐? 아니면 len(S)-i이냐?
        myString=S[j:j+i]
        #print(myString)
        possibles.add(myString)

print(len(possibles))