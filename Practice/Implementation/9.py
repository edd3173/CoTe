"""
문자열 압축.
HARD!
"""



def solution(s):
    answer=len(s)
    max_cut = len(s)//2+1
    #print(max_cut)
    for i in range(1,max_cut):  #  1~n개 단위로 자를때. max는 s//2. 6이라면 최대 3까지 자를 수 있다. 따라서 마지막에 +1
        # For 1~max_half, try to find repetition
        comp = "" # 줄어든 문자열
        prev = s[0:i] # 처음부터 i만큼 자른 문자열.
        cnt = 1 # 반복된 문자 숫자
        
        for j in range(i,len(s),i): # j의 시작은 i부터 끝까지, step은 i. 왜? 왜 1이 아니지? 
            #'abcabcdede'에서 prev는 [ab], s[j:j+i](new)는 [ca]
            # 그 다음 for에서 prev는 [ca]이고, s[j:j+i](new)는 [bc]가 되어야 한다.
            # 따라서 j의 step역시 i와 같아야. 만약 그렇지 않다면,
            # prev = [ca] s[j:j+i]=[ab] 같은 서로 영역이 겹치는 상황 발생.
            print("prev:",prev)
            if prev == s[j:j+i]: # CMP(s[0:i],s[j:j+i] 합리적. j :(2,10,2)
                print("Matched!")
                print("i:",i,"j:",j)
                print(prev, s[j:j+i])
                cnt+=1
            else:
                comp += str(cnt)+ prev if cnt>=2 else prev
                prev=s[j:j+i] # 이걸 업데이트 하면서 문제를 해결했는데, 
                cnt=1
                
        comp += str(cnt) + prev if cnt >=2 else prev
        answer = min(answer,len(comp))
                
        # for aabbaccc
        # we found aa. then start moves at bb. need to update pos.
        # then we do the same thing. 
        # how to make this loop?
        

    return answer



#s="aabbaccc"
#s="ababcdcd/ababcdcd"
s="abcabcdede"
#s="abcabcabcabcdededededede"
#s="xababcdcdababcdcd"

print(solution(s))