n,c = map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))

arr.sort()

# 1,2,4,8,9

start = arr[1]-arr[0]
end = arr[-1]-arr[0]

def binary_search(arr,start,end):
    result=-1
    while start<=end:
        cnt=1
        val = arr[0]
        currentGap = (start+end) // 2
        
        # Key Point
        for i in range(1,n):
            if arr[i] >= val+currentGap:
                cnt+=1
                val = arr[i]
                
        if cnt >= c:
            start = currentGap + 1
            result = currentGap
        else:
            end = currentGap - 1
    return result

ans = binary_search(arr,start,end)
print(ans)