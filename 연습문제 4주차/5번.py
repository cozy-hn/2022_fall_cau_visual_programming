N=float(input("N=?"))
list=[]
for i in range(0,5):
    list.append(N%10)
    N//=10
list.reverse()
print("%d만" %list[0])
print("%d천" %list[1])
print("%d백" %list[2])
print("%d십" %list[3])
print("%d" %list[4])

      
