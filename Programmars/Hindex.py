def solution(citations):
    answer=-1
    citations.sort(reverse=True)
    #print(citations)
    possible=[]
    for h in range(len(citations),-1,-1): # 최대 배열 길이만큼 나타날 수 잇으니까..
        upper=[]; lower=[];
        for c in citations:
            if c>=h: 
                upper.append(c)
            else:
                lower.append(c)
        #print("h:",h)
        #print("upper:",upper)
        #print("lower",lower)
        if len(upper) >= h and len(lower) <= h:
            possible.append(h)
    #print(possible)
    answer = max(possible)
    return answer

