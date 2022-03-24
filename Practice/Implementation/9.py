
def solution(s):
    
    length=len(s)
    ans=length
    
    # 몇개 단위로 잘라보냐?
    # 1 ~ n/2 가 최대일듯
    for l in range(1,length//2+1):
        #잘라보자
        comp=""
        target = s[:l]
        repetition=1 # 기본횟수는 1
        for j in range(l,len(s),l):
            if target == s[j:j+l]: # substr 0~l, l~2l is same
                repetition+=1 # ab가 여러번 반복.
                # 계속 s[j:j+l]은 j가 업데이트 되면서 다음 피스를 찾음.
                # 주의할 점은 타겟은 고정이라는거.
            else: # 찾을 수 없을때 타겟이 바뀌는거지.
                if repetition >=2: # 단 1ab는 그냥 ab니까!
                    curChunk = str(repetition)+target
                else:
                    curChunk = target
                    
                comp+=curChunk
                # s[j+l:j+2l]이 아닌이유? 지금 s[j:j+l]을 보고있는데.
                # 타겟과 드리나까, 지금 보고 있는 것을 새 타겟으로 삼아야.
                target = s[j:j+l]
                repetition = 1 # 기본횟수는 1
            
        # if로 상황이 끝났을 때에, 축약문자열을 만들지 않고 끝낼수 있다.
        # 따라서 처리를 한번 더해줘야됨
        if repetition >=2: # 단 1ab는 그냥 ab니까!
            curChunk = str(repetition)+target
        else:
            curChunk = target
        comp+=curChunk
        # 그러니 repetition=1은 넣을 필요가 없지
        ans = min(ans,len(comp))
            
    return ans


s=["aabbaccc","ababcdcdababcdcd","abcabcdede","abcabcabcabcdededededede","xababcdcdababcdcd"]
for string in s:
    result=solution(string)
    print(result)
