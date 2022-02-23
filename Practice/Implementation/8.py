"""문자열 재정렬"""
"""
POINTS:

1) To Check Alpha Or Digit

character.isalpha()
character.isdigit()

2) List comprehension
Chars+=ch is fine, but USE Chars.append(ch) 
because Chars here is list, not a string.

"""




String=input()
alphabets=[]
numbers=[]
for Char in String:
  if Char.isalpha() == True:
    alphabets.append(Char)
  elif Char.isdigit() == True:
    numbers.append(int(Char))
    
alphabets.sort()

"""
Rather than

Alpha=""
for Char in alphabets:
  Alpha+=str(Char)
  
USE JOIN!
out = str(_some_list) not works!
-> out = ''.join(_some_list)
"""


Alpha=''.join(alphabets)

Sum=sum(numbers)

if Sum!=0:
  print(Alpha+str(Sum))
else:
  print(Alpha)


