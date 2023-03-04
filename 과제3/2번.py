import random
from datetime import datetime


fdic=open('dict_test.TXT','r')
diclist=fdic.readlines()
fdic.close #리스트로 가져오고 파일 닫음
dicdic={} #사전들어갈 딕셔너리, 딕셔너리쓰면 중복 자동 제거
for i in diclist:
    n=i.index(':')
    if n==len(i)-2: #biosph : 제거
        continue
    dicdic[i[0:n-1]]=i[n+2:]

    if (dicdic[i[0:n-1]][0]=="I"):
        del dicdic[i[0:n-1]]
dickeylist=list(dicdic.keys())


cnt=0
sum=0
while cnt<10:
    cnt+=1
    rannum=random.randrange(7,11)
    ranlist=random.sample(dickeylist,rannum)
    question=""
    for i in ranlist:
        question=question+i+" "
    question = question[:-1]
    print("(%d/10)타자게임! 사전에서 랜덤으로 선택된 7~10개의 단어를 그대로 치세요" %cnt) #사전에 띄어쓰기 있는 단어들이 있어서 10개 넘어 보일 수도 있음 하지만 10개 추출
    dtstart = datetime.now()
    print("= %s" %question)
    ans=input("= ")#마지막 띄어쓰기 제거
    dtend=datetime.now()
    timedel=dtend-dtstart
    time=timedel.total_seconds() #타이핑 친 초
    typespeed=len(ans)*60/time #타/초 >>타이핑한 길이/초  //타/분 >> 타/초 * 60 
    if question==ans:
        score=(20-time)*1000
        if time>20:
            print("시간 초과! 시간 : %ld" %time)
            score=0
        print("맞았습니다.(%lf점 획득 %lf타/분)" %(score, typespeed))
    else:
        score=0
        buf=0
        if len(question)<len(ans):
            min=len(question)         
        else:
            min=len(ans)
        for i in range(0,min):
            if question[i]!=ans[i]:
                print(" "*(i+2)+"^")
                buf=1
                break
        if buf==0:
            print(" "*(min+2)+"^")
        print("틀렸습니다.(%lf타/분)" %typespeed)
    sum=sum+score
print("당신의 총 점수는 %lf점 입니다." %sum)
    

