

''' 동전 거슬러주기'''




# My Code

"""
total=1260

fh=total//500
total-=fh*500

oh=total//100
total-=oh*100

ft=total//50
total-=ft*50

tn=total//10
total-=tn*10

if(total!=0):
  print("Something Wrong!")
else:
  print(fh+oh+ft+tn)

"""


# Book Code

n=1260
count=0

arr=[500,100,50,10]


for coin in arr:
  count += n // coin #This is okay
  n%=coin # same as total -= COIN_VAL * COIN_NUM

print(count)