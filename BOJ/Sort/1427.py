N = input()

myList = list(str(N))
myList.sort(reverse=True)
myStr = "".join(myList)
print(myStr)
