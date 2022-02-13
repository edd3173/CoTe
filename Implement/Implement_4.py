"""문자열 재정렬"""

data=input()

Sum=0
#List
Chars=list()
# or, Chars=[]

for ch in data:
  if ch >= '1' and ch <= '9':
    Sum+=int(ch)
  else:
    Chars+=ch
    #Chars.append(ch)
    # Or, we can use Chars.append(ch)

"""
POINTS:

1) To Check Alpha Or Digit

character.isalpha()
character.isdigit()

2) List comprehension
Chars+=ch is fine, but USE Chars.append(ch) 
because Chars here is list, not a string.

"""




Chars.sort()
#print(Chars)
#print(Sum)

# SEPERATOR.JOIN(ITERABLE) returns single string
Str=''.join(Chars)

# CHECK!!! Sum may be 0
if Sum!=0:
    ans=Str+str(Sum)
else:
    ans=Str
    
print(ans)