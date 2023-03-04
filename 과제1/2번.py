Dong=['흑석동', '사당동', '상도동', '노량진동', '규동']
length=len(Dong)
while True:
    data=input("동을 입력하세요. ")
    if(data in Dong):
        print(Dong.index(data)+1,"번째 동입니다.", sep='')
    else:
        print("새로운 동명입니다.", length+1, "번째 동으로 등록합니다.", sep='')
        length+=1
        Dong.append(data)

#종료에 관한 조건이 없어서 종료코드는 안 넣었습니다



