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



data = input()

alphabets=[]
numbers=[]

for ch in data:
  if ch.isdigit():
    numbers.append(int(ch))
  if ch.isalpha():
    alphabets.append(ch)

alphabets.sort()
sumVal = sum(numbers)
#print(sumVal)

alphabetString = "".join(alphabets)
if sum == 0:
  ans = alphabetString
else:
  ans = alphabetString + str(sumVal)

print(ans)

