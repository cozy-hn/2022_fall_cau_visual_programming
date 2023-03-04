filename="test.txt"
f=open(filename,'r')
fli=f.readlines() #라스트 출력
f.close()
for i in range(len(fli)): #개행문자 제거
    fli[i]=fli[i][:-1]
print(fli)

    