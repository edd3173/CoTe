"""
1. 큰 틀을 잡는건 거의 비슷함
2. 자료구조 : 2차원 arr가 아니라, element에 집중함
3. check condition에서 배열을 다 찾지 않고, elem을 확인함으로 가능.

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