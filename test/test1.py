import sys

def findN(a,b):
    li=[]
    li.append([i for i in range(1,b+1)])
    for k in range(1,a+1):
        for i in range(b):
            if i==0:
                li.append([1])
            else:
                li[k].append(li[k-1][i]+li[k][i-1])
    print(li[a][b-1])

N=int(sys.stdin.readline())
for _ in range(N):
    a=int(sys.stdin.readline())
    b=int(sys.stdin.readline())
    findN(a,b)
