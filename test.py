def solution(new_id):
    answer = ''
    
    #step1
    new_id = new_id.lower()
    
    #step2
    for ch in new_id:
        if ch.isalpha() or ch.isdigit() or ch=='-' or ch=='_' or ch=='.':
            continue
        else:
            new_id = new_id.replace(ch,"")
    print(new_id)
    
    #step3
    targets=[]
    for i in range(len(new_id)-1):
        if new_id[i]=='.' and new_id[i+1]=='.':
            targets.append(i)
    
    for i in range(len(targets)):
        new_id = new_id.replace("..",".")
    print(new_id)
    
    #step4
    if new_id[0]=='.':
        new_id = new_id[1:]
    #print(new_id[-1])        
    
    print("["+new_id+"]")
    print(new_id[-1])
    
    return answer

myStr="...!@BaT#*..y.abcdefghijklm"
solution(myStr)