filename="test.txt"
f=open(filename,'a')
for i in range(1,4):
    f.write('ㅋ\n'*i)
f.close()