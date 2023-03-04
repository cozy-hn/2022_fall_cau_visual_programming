mylist = [ 23,78,43,11,94,73,13,87,67,16,8]
mid=mylist[len(mylist)//2]
mylist.sort()
avg=(mylist[0]+mylist[-1])/2
if mid>avg:
    print(mid)
elif avg>mid:
    print(avg)
else:
    print("두 값은 %d로 같습니다" %mid)