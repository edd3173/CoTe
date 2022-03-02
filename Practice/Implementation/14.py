"""
외벽점검



1. 원형에 대해서는 길이를 2배로 늘려 일자로 만들어준대

와 이건 봐도 모르겠다

"""

from itertools import permutations

def solution(n, weak, dist): # 봐도 모르겠군...
    for i in range(len(weak)):
        weak.append(weak[i]) # double
    answer = len(dist)+1 # like int(1e9)
    
    for friends in permutations(dist,len(dist)):
        for i in range(len(weak)):
            count = 1
            position = weak[i] + friends[count-1]
            for idx in range(i,i+len(weak)):
                if position < weak[idx]:
                    count +=1
                    if count > len(dist):
                        break
                    position = weak[idx] + friends[count-1]
            answer = min(answer,count)
        if answer>len(dist):
            return -1
    return answer


n=12
weak = [1,5,6,10]
dist = [1,2,3,4]
result = solution(n,weak,dist)
print(result)