import math
a,b,c = map(int,input().split())
"""
total = a + b*x
sold = c * x

sold >=  total
c-b x >=a
x > = a/(c-b)

""" 
if b>=c:
    print(-1)
else:
    print((a // (c-b))+1)
