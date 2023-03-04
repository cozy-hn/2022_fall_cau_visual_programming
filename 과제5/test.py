import sys
from collections import deque
dq=deque()
N=int(sys.stdin.readline())
for _ in range(N):
    oder=sys.stdin.readline().split()
    if oder[0]=='push':
        dq.append(oder[1])
    elif oder[0]=='pop':
        if len(dq)==0:
            print(-1)
        else:
            print(dq.popleft())
    elif oder[0]=='front':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0])
    elif oder[0]=='back':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])            
    elif oder[0]=='size':
        print(len(dq))
    elif oder[0]=='empty':
        if len(dq)==0:
            print(1)
        else:
            print(0)
