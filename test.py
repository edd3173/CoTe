"""
1 2 3
4 5 6
7 8 9

7 4 1
8 5 2
9 6 3
"""

import copy


def rotateMatrix(myMat):
    length = len(myMat[0])
    newMat = []
    for i in range(length):
        curRow=[]
        for j in range(length):
            curRow.append(myMat[j][i])
        curRow.reverse()
        newMat.append(curRow)
    return newMat

def isValid(board):
    # for middle of board, check if value is all '1'
    length = len(board[0])
    startIdx = length // 3
    endIdx = startIdx * 2
    
    for i in range(startIdx,endIdx): # NOT endIdx+1.
        for j in range(startIdx,endIdx):
            if board[i][j] != 1:
                return False
    return True                    
                        
            

def solution(key,lock):
    lockLength = len(lock[0])
    keyLength=len(key[0])
    augLockLength = 3 * lockLength
    augLock = [[0] * augLockLength for _ in range(augLockLength)]
    
    # make augmented lock
    for i in range(lockLength):
        for j in range(lockLength):
            augLock[i+lockLength][j+lockLength] = lock[i][j]
    
    for rotation in range(4):
        key = rotateMatrix(key)
        """
        augLockLength-keyLen이 아님.
        key는 어디부터 어디까지 움직이느냐?
        lock의 끄트머리에 걸칠 수 있는 부분까지 움직일 수 있다.
        """   
        for i in range(2*lockLength):
            for j in range(2*lockLength):
                for k in range(keyLength):
                    for l in range(keyLength):
                        augLock[i+k][j+l] += key[k][l] # board는 절대좌표다 k,l은 상대좌표
                
                """
                k,l 문 안에서 check(augLock[][],key[][])를 하면 망한다!
                왜? 전체 k와 auglock에 대해 판단을 해야지,
                k의 원소 단위에서 판단하면 파편화 발생해서 틀림!
                추가로, 딥카피 쓰지마 그냥;;
                
                """
                
                # board에 값 대입 후에 해봐야됨        
                res = isValid(augLock)
                if res==True:
                    return True
                
                
                
                for k in range(keyLength):
                    for l in range(keyLength):
                        augLock[i+k][j+l] -= key[k][l]

                
    return False

    


key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key,lock))