"""
Subset Sum
"""

n=5
data=[10,20,30,40,50]

sum=0
psum=[0]

for i in data:
    sum+=i
    psum.append(sum)
    
left=3; right=4
print(sum[right]-sum[left-1])