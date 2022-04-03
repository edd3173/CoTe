arr = [1, 2, 2, 2, 3, 3, 4, 6]

cnt=0

for a in arr:
    if a == 2:
        arr.remove(a)
        cnt+=1

print(arr)
print(cnt)