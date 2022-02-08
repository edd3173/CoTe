"""
Replace Two Arrays
"""

n,k = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Replace A's min elem with B's max elem. If later is bigger.

A.sort() # Ascending Order
B.sort(reverse=True) # Descending Order

for i in range(0,k):
  if(A[i]<=B[i]):
    A[i]=B[i]

print(A)
print(B)

print(sum(A))
    
