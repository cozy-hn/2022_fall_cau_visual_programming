N=int(input())
tmp=N
cnt=0
while True:
    cnt+=1
    sumN=N//10+N%10
    N=(N%10)*10+sumN%10
    if tmp==N:
        break
print(cnt)