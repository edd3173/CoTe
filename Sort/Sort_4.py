"""
성적 낮은 순서로 출력
python의 tuple을 사용할 줄 알아야.
"""


def _key(data):
    return data[1]





n=int(input())

arr=[]
for i in range(n):
    data=input().split()
    arr.append((data[0],int(data[1])))
    
# lambda 매개변수 : 표현식
arr=sorted(arr,key=lambda student: student[1])

# By key_func
arr=sorted(arr,key=_key)


for i in range(n):
    print(arr[i][0],end=' ')