ca=[ "c=","c-","dz=","d-","lj","nj","s=","z="]
letters=input()
for cl in ca:
    if cl in letters:
        letters=letters.replace(cl,'*')

print(len(letters))