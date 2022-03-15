from bisect import bisect_left, bisect_right

def countByRange(arr,leftVal,rightVal):
    leftIdx=bisect_left(arr,leftVal)
    rightIdx=bisect_right(arr,rightVal)
    return rightIdx - leftIdx


arr=[[] for _ in range(10001)]
reversedArr = [[] for _ in range(10001)]

def solution(words,queries):
    answer=[]
    for word in words:
        arr[len(word)].append(word)
        reversedArr[len(word)].append(word[::-1])
    
    for i in range(10001):
        arr[i].sort()
        reversedArr[i].sort()
        
    for query in queries:
        if query[0]=='?':
            res = countByRange(reversedArr[len(query)],query[::-1].replace('?','a'),query[::-1].replace('?','z'))
        else:
            res = countByRange(arr[len(query)],query.replace('?','a'),query.replace('?','z'))
        answer.append(res)
    return answer

words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries=["fro??", "????o", "fr???", "fro???", "pro?"]
result = solution(words,queries)
print(result)