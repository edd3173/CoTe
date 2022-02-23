
''' 1이 될 때까지'''

n,k = map(int,input().split())
ans=0

print(n,end=' ')
while n != 1:
  if n==1:
    break
  if n%k == 0:
    n//=k; ans+=1
    print(n,end=' ')
  else:
    n-=1; ans+=1
    print(n,end=' ')
print()  
print(ans)


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

#T
