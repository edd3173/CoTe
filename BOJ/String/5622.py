data={}

for i in range(3):data[chr(ord('A')+i)]=2
for i in range(3):data[chr(ord('D')+i)]=3
for i in range(3):data[chr(ord('G')+i)]=4
for i in range(3):data[chr(ord('J')+i)]=5
for i in range(3):data[chr(ord('M')+i)]=6
for i in range(4): data[chr(ord('P')+i)]=7
for i in range(3): data[chr(ord('T')+i)]=8
for i in range(4): data[chr(ord('W')+i)]=9

#print(data)

letters=input()
answer=0
for ch in letters:
    answer+=data[ch]
    answer+=1

print(answer)