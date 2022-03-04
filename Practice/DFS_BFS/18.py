"""
괄호변환
"""

def getBalancedIdx(p):
    cnt=0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -=1
        if cnt == 0:
            return i

def isProper(p):
    cnt=0
    for i in range(len(p)):
        if p[i]=='(':
            cnt+=1
        elif p[i]==')':
            if cnt == 0:
                return False
            cnt -=1
    return True

def solution(p):
    answer = ''
    if p == "":
        return answer
    
    idx = getBalancedIdx(p)
    u = p[:idx+1]
    v = p[idx+1:]
    
    if isProper(u):
        return u+solution(v)
    else:
        answer = '(' + solution(v) + ')'
        
        u = list(u[1:len(u)-1]) # we convert to string
        
        for i in range(len(u)):
            # since this doesn't work in normal string:
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        
        # As a result, we use "".join() to concat
        answer += "".join(u)
        return answer



p = "(()())()"
p = ")("
p = "()))((()"
result = solution(p)
print(result)



"""
너무 쫄지마!
그런데 그 technique는 알아야 한다.
string은 마음대로 값 변경이 안되기 때문에
list()로 변환시켜서 값 변경,.
그리고 나서 "".join()을 사용
"""