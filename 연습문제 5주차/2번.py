N=int(input("N=? "))
X=int(input("X=? "))
list=[]
for i in range(0,10):
    num=int(input())
    list.append(num)
for i in list:
    if i<5:
        print("%d " %i, end="")