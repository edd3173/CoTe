s = input()

answer = [-1] * 26

"""
join을 쓰는 법.
그리고 정수의 list는 바로 string으로 전환하기 어려움!

"""
for i in range(ord('a'),ord('z')+1):
    ch = chr(i)
    idx = i-ord('a')
    answer[idx] = s.find(ch)

temp = [str(ch) for ch in answer]
res = ' '.join(temp)
print(res)