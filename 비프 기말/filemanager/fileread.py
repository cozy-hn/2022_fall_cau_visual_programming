filename="test.txt"
f=open(filename,'r')
fstr=f.read()#전체읽기
f.close()
print(fstr)

filename="test.txt"
f=open(filename,'r')
fstr=list(f.read().split("\n"))[:-1] #리스트형
f.close()
print(fstr)