def solution(citations):
    answer=-1
    citations.sort(reverse=True)
    #print(citations)
    possible=[]
    for h in range(max(citations),min(citations)-1,-1):
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
    print(possible)
    answer = max(possible)
    return answer


citations=[10,10,10,10,10]
#citations=[0,0,0,0,0]
print(solution(citations))