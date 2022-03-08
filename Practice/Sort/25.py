"""
실패율


쉽게 짜자 제발 쉽게!!!

"""

def solution(N,stages):
    answer=[]
    length = len(stages)
    
    for i in range(1,N+1):
        count = stages.count(i)
        
        if length ==0:
            fail = 0
        else:
            fail = count / length
        
        answer.append(i,fail)
        length -= count
    
    answer = sorted(answer,key = lambda x:x[1],reverse= True)
    
    answer = [i[0] for i in answer]
    return answer

"""

더 좋은 코드. 교재를 보고 배우자.

def solution(N, stages):
    answer = []
    UserNum=len(stages)
    myStages = [0] * UserNum
    
    # copy for later use
    for i in range(UserNum):
        myStages[i]=stages[i]
    
    stages.sort()
   
    Failed = [0] * (N+2)
    Numbers = [-1] * UserNum
    while stages:
        Failed[stages[0]] += 1
        stages.pop(0)
    
    #print(Failed)
    
    for i in range(UserNum):
        sub = Failed[0:i]
        Numbers[i] = UserNum - sum(sub)
    
    #print(Numbers)
    
    myArr = [[0,0]]
    
    for i in range(1,N+1):
        myArr.append([i, Failed[i]/Numbers[i]])
    myArr.pop(0)
    myArr.sort(key = lambda x:x[1], reverse=True)
    #print(myArr)
    
    for ele in myArr:
        answer.append(ele[0])
        
    return answer



N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]
result=solution(N,stages)

"""