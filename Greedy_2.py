
data=list(map(int,input().split()))

print(data)

n=data[0]
k=data[1]
ans=0

'''
책 코드
while True: # Why not 1? b/c leftover
  #Nearest 배수
  target=(n//k) * k

  # 그냥 % 때리면 되는거 아녀?
  ans += n - target
  
  # N을 가장 가까운 배수로 바꿈.
  n=target

  # 이제 나눠야 하는데, 더 못나눌 수 있다
  if n<k:
    break
  
  #나눌 수 있다
  ans+=1
  n//=k

# Leftover 처리.
ans+= (n-1)
print(ans)

'''

#This looks better

while n!=1: #Until become 1
    if k<=n: # when k>n, able to devide
        if n%k ==0:
            ans+=1
            n//k
        else:
            ans+=n%k
            n-=n%k
    else: #Last case, when n<k, can't devide
        ans+=n-1 #Substract
        n=1 #To finish loop
        
print(ans)
