list=[]
while True:
    A=int(input("A=? "))
    B=int(input("B=? "))
    if (A+B)==0:
        break
    list.append("%d+%d=%d" %(A,B,A+B))
for i in list:
    print(i)
