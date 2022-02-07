
"""
Selection Sort
"""


arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
        if arr[j]<=arr[min_idx]: #find index
            min_idx=j
        #swap values of idx
    #tmp=arr[i]; arr[i]=arr[min_idx]; arr[min_idx]=arr[i]
    # Or Swap like this: Worth Study
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)


"""
Insertion Sort
"""

arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(arr)): # 5,9,0,3 ...
    for j in range(i,0,-1): # 5에서 역방향으로 -1씩 이동
        if arr[j]<=arr[j-1]: # 현재 idx(현재)와 idx-1(왼쪽)의 val을 비교. 어 idx가 더 작네?
            arr[j], arr[j-1] = arr[j-1, j] # 그럼 왼쪽으로 가야지
        else: # 어 이제 왼쪽거보다 지금이 더 큰데?
            break # 그럼 이동할 필요없지
print(arr)


"""
Quick Sort
"""

