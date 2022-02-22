"""
Two Pointer - Hard
"""

n=5; m=5
data=[1,2,3,2,5]

cnt=0
subsum=0
start=0
end=0

for start in range(n):
    while subsum < m and end<n:
        subsum+=data[end]
        end+=1
    if subsum==m:
        cnt+=1
    subsum-=data[start]
    
print(cnt)