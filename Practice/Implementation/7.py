
"""
Pelindrome
Easy
"""

N=input()

# len 6? idx 3.
centIdx=len(N)//2
#print(centIdx)

Left = 0
for i in range(0,centIdx):
  Left+=int(N[i])

Right=0
for j in range(centIdx, len(N)):
  Right+=int(N[j])

#print(Left,Right)

if Left==Right:
  print("LUCKY")
else:
  print("READY")