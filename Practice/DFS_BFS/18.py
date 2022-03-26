

def isBalanced(p):
    leftCount = p.count('(')
    rightCount = p.count(')')
    if leftCount==rightCount: return True
    else: return False

def isCorrect(p):
    Count=0
    for i in range(len(p)):
        if p[i]=='(':
            Count+=1
        if p[i]==')':
            if Count==0:
                return False
            Count-=1
    if Count !=0: # need not, but good job.
        return False
    return True

def findBalancedIdx(p):
    count=0
    for i in range(len(p)):
        if p[i]=='(': count+=1
        if p[i]==')': count-=1
        if count==0: return i


def solution(p):
    if not p: return p
    idx = findBalancedIdx(p)
    u = p[:idx+1]
    v = p[idx+1:]
    if isCorrect(u): 
        return u+solution(v)
    else:
        temp="("+solution(v)+')'
        u=list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        temp+="".join(u)
        return temp

#p = "(()())()"
#p = ")("
p = "()))((()"
result = solution(p)
print(result)
