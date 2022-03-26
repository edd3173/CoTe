"""
1. 큰 틀을 잡는건 거의 비슷함
2. 자료구조 : 2차원 arr가 아니라, element에 집중함
3. check condition에서 배열을 다 찾지 않고, elem을 확인함으로 가능.

"""
"""
정답코드는 pillar, archs를 따로 정의하는게 아니라,
answer[]에 하나로 저장함.
어떻게? (x,y)만 저장하는게 아니라 숫자 0,1을 추가하는 방식으로 ㅇㅇ.

로직 꼼꼼히 보기.
"""


def possible(answer):
    for x,y,stuff in answer:
        if stuff == 0: # pillar check
            # on land, above pillar, on beam x 2
            if y==0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer: 
                continue
            return False
        
        if stuff == 1: # beam
            # on pillar x 2, on beam x 2
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False

    return True


def solution(n, build_frame):
    answer=[]
    for frame in build_frame:
        x,y,stuff,operate = frame
        
        if operate == 0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
                
        if operate == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
                
    return sorted(answer)


n=5
build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n,build_frame))



"""
MyCode


pillars=[]
archs=[]

def check(): # check big view if its okay
    pillarFlag=True
    archFlag=True
    # Pillar conditions
    for pillar in pillars:
        px,py = pillar
        if py==0 or (px,py-1) in pillars or (px-1,py) in archs or (px,py) in archs:
            continue
        else:
            pillarFlag=False
             
    #arch condition
    for arch in archs:
        ax,ay = arch
        if (ax,ay-1) in pillars or (ax+1,ay-1) in pillars or ((ax-1,ay) in archs and (ax+1,ay) in archs):
            continue
        else:
            archFlag=False
    
    if pillarFlag and archFlag:
        return True
    else:
        return False

def solution(n, build_frame):
    result=[]
    
    # process data
    for frame in build_frame:
        x,y,a,b = frame
        if a==0: # pillar
            if b==0: # delete
                pillars.remove((x,y))
                res = check() # (x,y)를 전달안해줘도되나?
                if res==False:
                    pillars.append((x,y))
            elif b==1: # install
                pillars.append((x,y))
                res = check()
                if res==False:
                    pillars.remove((x,y))
        elif a==1: # arch
            if b==0: # delete
                archs.remove((x,y))
                res = check() # (x,y)를 전달안해줘도되나? ㅇㅇ. 판단하고 아니면 취소
                if res==False:
                    archs.append((x,y))
            elif b==1: # install
                archs.append((x,y))
                res = check() # (x,y)를 전달안해줘도되나?
                if res==False:
                    archs.remove((x,y))
    
    for pillar in pillars:
        x,y = pillar
        z = 0
        result.append([x,y,z])
    for arch in archs:
        x,y = arch
        z = 1
        result.append([x,y,z])
    result.sort()
    return result
"""