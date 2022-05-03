s = input()
occurence = [0] * 26
s=s.upper()

for ch in s:
    idx = ord(ch)-ord('A')
    occurence[idx]+=1

#print(occurence)

if occurence.count(max(occurence))!=1:
    print('?')
else:
    maxIdx = occurence.index(max(occurence))
    maxIdx+=ord('A')
    print(chr(maxIdx))
    