
N,M = map(int,input().split())

myList=[]

def dfs(myList):
    if len(myList)==M:
        for e in myList:
            print(e,end=' ')
        print()
        return
    for i in range(1,N+1):
        if i not in myList:
            myList.append(i)
            dfs(myList)
            myList.pop()
            
dfs(myList)