N,M = map(int,input().split())
nData=[]
for _ in range(N):
    nData.append(input().strip())
mData=[]
for _ in range(M):
    mData.append(input().strip())

nData=set(nData); mData=set(mData);
IS = nData.intersection(mData)
IS = sorted(IS)
print(len(IS))
for e in IS:
    print(e)
    
    
    """
    뭔가 정렬된 상태로 출력할 때는 set을 쓰는것을 지양하자.
    """