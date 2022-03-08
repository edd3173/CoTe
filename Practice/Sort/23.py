"""
국영수
"""

n=int(input())
arr=[]

for _ in range(n):
    name,k,e,m = list(input().split())
    arr.append((name,k,e,m))
    
    
"""
Important Technique
똑같은걸 key로 4번 할 수 있는데, 그러면 아마 안되겠지.
따라서 우선순위를 맞춰 정렬한다.

lambda를 쓰는 방법, 그리고 lambda에서 우선순위를 맞춰 sort하는 방법.
꼭 숙지하자.

"""

arr.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(arr[i][0])