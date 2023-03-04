fdic=open('dict_test.TXT','r')
diclist=fdic.readlines()
fdic.close #리스트로 가져오고 파일 닫음
dicdic={} #사전들어갈 딕셔너리, 딕셔너리쓰면 중복 자동 제거
for i in diclist:
    n=i.index(':')
    if n==len(i)-2: #biosph : 제거
        #print("뜻이 담겨있지 않습니다 %s\n" %i[0:n-1])
        continue
    dicdic[i[0:n-1]]=i[n+2:]

    if (dicdic[i[0:n-1]][0]=="I"):
        #print("다음 단어의 뜻이 I가 아닙니다 : %s, %s" %(i[0:n-1],i[n+2:])) #뜻이 I로 시작하는 깨진것들 제거
        del dicdic[i[0:n-1]]
while True:
    wantfind=input("단어? ")
    if (wantfind in dicdic):
        print("%s %s" %(wantfind,dicdic[wantfind]),end='')
    else:
        print("찾으려는 단어가 없습니다")
