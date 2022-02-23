def rotate_matrix(a):
    """
    #Init new_mat
    k=len(key[0])
    #print(k)
    #new_mat = [[0]* k for _ in range(k)]
    new_mat=[]
    #print(new_mat)
    # for each col, replace it to new row
    
    for i in range(k):
        cur_col=[]
        for j in range(k-1,-1,-1):
            cur_col.append(mat[j][i])
        new_mat.append(cur_col)
    return new_mat
    """
    
    n=len(a)
    m=len(a[0])
    result=[[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1]=a[i][j]
    return result

def check_cond(combined_matrix):
    new_n=len(combined_matrix[0])
    start=new_n//3
    end=new_n//3 * 2
    for i in range(start,end):
        for j in range(start,end):
            if combined_matrix[i][j]!=1:
                return False
    return True

def solution(key, lock):
    m=len(key[0])
    n=len(lock[0])
    
    # Expand Lock to new_lock
    new_n=3*len(lock[0])
    new_lock = [[0]*new_n for _ in range(new_n)]
    #print(new_lock)
    
    # Input val of original lock
    start=new_n//3
    end=(new_n//3) * 2
    
    for i in range(start,end):
        for j in range(start,end):
            new_lock[i][j]=lock[i-start][j-start]
    #print(new_lock)
    
    # for every rotation
    for rotate in range(4): # rotate 4 time
        
        key=rotate_matrix(key) # rotated
        combined_mat=new_lock # combined puzzle
        #print(new_lock)
        #print(combined_mat)
        
        for i in range(0,new_n-n): # in new_lock
            for j in range(0,new_n-n): # in new_lock
            
                for k in range(0,m):
                    for l in range(0,m): # for each array of key
                        
                        combined_mat[i+k][j+l] = new_lock[i+k][j+l] + key[k][l] # make combined
                        res = check_cond(combined_mat) # check condition
                        
                        if(res==True):
                            return True
        print(new_lock)
        
    return False



key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

solution(key,lock)