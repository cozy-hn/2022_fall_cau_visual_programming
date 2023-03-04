N=int(input("N=?"))
fact=1
for i in range(1,N+1):
    fact*=i
    print("%d!=%d" %(i,fact))