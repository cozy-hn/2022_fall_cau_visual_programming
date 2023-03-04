N=int(input("N=?"))
num=1
for i in range(1,N+1):
    print(" "*(N-i+1), end="")
    for j in range(1,i+1):
        print("%d " %num ,end="")
        num+=1
    print("")