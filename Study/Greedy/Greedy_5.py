""" 큰 수의 법칙 """


n,m,k = map(int,input().split())
data=list(map(int,input().split()))

#For Convenience
data.sort(reverse=True)
print(data)

#Biggest two
first=data[0]
second=data[1]

#Ans 
ans=0

#Add #k at max times, total #m

"""
3 - 1 - 3 - 1 ... until max m

Or just do like this

n,m,k = map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()

first=arr[n-1]
second=arr[n-2]

chunk_num = m // (k+1)
remain_num = m % (k+1)

print(chunk_num, remain_num)

chunk_sum = first * k + second * 1
remain_sum = first * remain_num

SUM = chunk_sum * chunk_num + remain_sum
print(SUM)



"""

Iter=0

while True: #Looks break is easier than iteration
  for f in range(0,k):
    if(Iter==m): #Iter may == m inside the for loop, not the outside. so we need to deal.
      break
    ans+=first
    Iter+=1
  if(Iter==m): # and here
    break #The Double breaks
  ans+=second
  Iter+=1

print(ans)
  



