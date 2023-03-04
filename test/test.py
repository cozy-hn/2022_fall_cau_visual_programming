N=int(input())
opnum=N//5
if N%5==0:
    print(opnum)
elif N%5==1:
    opnum+=1
    print(opnum)
elif N%5==2:
    if N==7:
        print(-1)
    else:
        opnum+=2
        print(opnum)
elif N%5==3:
    opnum+=1
    print(opnum)
else:
    if N==4:
        print(-1)
    else:
        opnum+=2
        print(opnum)
        