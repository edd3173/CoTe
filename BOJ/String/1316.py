
def isSequentialIndex(indexes):
    # determine if certain alphabet's index are sequential
    if len(indexes)==1:
        return True
    else:
        for i in range(len(indexes)-1):
            if indexes[i+1]-indexes[i]!=1:
                return False
    return True

numbers = int(input())
answer=0

for n in range(numbers):
    
    # get number input
    word = input()
    
    # dict of pair : { alphabet : indexes_appeared_in_word}
    chIdx={}
    
    # iterate word
    for i in range(len(word)):
        # if alphabet not registered in dict
        if word[i] not in chIdx.keys():
            # create new pair of alphabet
            chIdx[word[i]]=[i]
        # if not
        else:
            # append index to pair
            chIdx[word[i]].append(i)
    #print(chIdx)
    
    # check if alphabets of word is sequential
    Flag=True
    
    # iterate through alphabets
    for val in chIdx.values():
        # check if alphabet's indexes are sequential
        res = isSequentialIndex(val)
        #print(res)
        # if not,
        if not res:
            # set flag to false
            Flag=False
    # if word's alphabets' indexes are all sequential, set answer
    if Flag:
        answer+=1

print(answer)