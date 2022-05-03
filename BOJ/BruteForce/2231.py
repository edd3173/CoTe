
def generate(num):
    res=num
    num = str(num)
    for n in num:
        res += int(n)
    return res    

N=int(input())

"""
216의 분해합 : 216 + 2 + 1 + 6 = 225
216는 225의 생성자

245의 분해합 : 245 + 2 + 4 + 5 = 256
245는 256의 생성자

given N
N의 가장 적은 생성자 M
M의 분해합 : N
M은 N의 생성자.
가장 작은 M을 찾아야.

198 + 9 + 8 = 216

"""
Flag=False
for i in range(N):
    if generate(i)==N:
        print(i)
        Flag=True
        break
    
if not Flag:
    print(0)



