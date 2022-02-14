"""
왕실의 나이트
"""
# dx,dy style
dx=[+1,+1,-1,-1,+2,+2,-2,-2]
dy=[+2,-2,+2,-2,+1,-1,+1,-1]

# move_set style
moves=[(+1,+2),(+1,-2),(-1,+2),(-1,-2),(+2,+1),(+2,-1),(-2,+1),(-2,-1)]
cnt=0

pos=input()
py=pos[0]; px=pos[1]

# match to (0,0)
# Remeber The ord() function!
py=ord(pos[0])-ord('a'); px=int(px)-1
#print(px,py)

for move in moves:
    nx=px+move[0]
    ny=py+move[1]
    
    if nx<0 or nx>=8 or ny<0 or ny>=8:
        continue
    else:
        cnt+=1

print(cnt)


