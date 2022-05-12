from lib2to3.pgen2.literals import evalString


data=input()

Numbers=[]; Operations=[]

start=0; end=0;
for i in range(len(data)):
    if data[i].isdigit():
        end=i
    else:
        curNum=int(data[start:i])
        curOper=data[i]
        start=i+1
        end=i+1
        Numbers.append(curNum)
        Operations.append(curOper)
    
    if i==len(data)-1:
        curNum=int(data[start:i+1])
        Numbers.append(curNum)

#print(Numbers)
#print(Operations)

myList=[]
start=0; end=0;
for j in range(len(data)):
    if data[j].isdigit():
        end=j
    else:
        curNum=int(data[start:j])
        curOper=data[j]
        start=j+1; end=j+1
        myList.append(curNum)
        myList.append(curOper)
    if j==len(data)-1:
        curNum=int(data[start:j+1])
        myList.append(curNum)

#print(myList)

"""
+ - (+ +)
+ + + 괄호 x
- - - 괄호 x

a - (b+c)
a + b-c 
a-b-c+d
a+b -c -d
a-(b+c)-d
a+b+c-d

30-40+50-60

"""
ans=0
if '-' not in Operations:
    ans=sum(Numbers)
elif '+' not in Operations:
    ans=Numbers[0]
    for i in range(1,len(Numbers)):
        ans-=Numbers[i]
else:
    # 그냥 덧셈을 미리 해
    while '+' in myList:
        for e in myList:
            if e == '+':
                firstIdx = myList.index(e)-1
                secondIdx = myList.index(e)+1
                first = myList[firstIdx]
                second = myList[secondIdx]
                myList.insert(myList.index(e),first+second)
                myList.pop(firstIdx); myList.pop(secondIdx); myList.pop(myList.index(e))
    
    stringList = [str(i) for i in myList]
    answerString = "".join(stringList).strip()
    #print("answerString:", answerString)
    ans=eval(answerString)
print(ans)