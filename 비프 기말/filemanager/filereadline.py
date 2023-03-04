filename="test.txt"
f=open(filename,'r')
while True:
    line=f.readline()[:-1] #한줄씩 출력
    if not line:
        break
    print(line)#개행문자 제거안하면 한줄씩 더 띄움
f.close()