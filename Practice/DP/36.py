


A=list(input())
B=list(input())

i = len(A); j = len(B)

"""
if A[i]==B[j]
DP[i][j] = DP[i-1][j-1]
else
DP[i][j] = min(DP[i-1][j]+1, DP[i][j-1]+1, )

"""