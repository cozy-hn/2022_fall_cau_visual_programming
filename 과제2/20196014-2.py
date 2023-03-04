intro=input("문장을 입력하세요 : ")
lenintro=len(intro)
if(lenintro>=31 and lenintro<=35): #*월 *일 ~ **월 **일까지 #이름 2글자 ~ 4글자까지 받음
    year=intro.find("년")
    month=intro.find("월")
    day=intro.find("일")
    print("분석된 생년월일: %s/%s/%s" % (intro[year-4:year], intro[year+2:month], intro[month+2:day]))
elif(lenintro>= 36 and lenintro<=38): #이름 2글자 ~ 4글자까지 받음
    print("분석된 생년월일: %s" % intro[intro.find("2"):intro.find("2")+10])
elif(lenintro>=25 and lenintro<=27): #이름 2글자 ~ 4글자까지 받음
    start=intro.find("2")
    print("분석된 생년월일: %s/%s/%s" %(intro[start:start+4],intro[start+4:start+6],intro[start+6:start+8] ))
else:
    print("형식에 맞지 않는 입력입니다. 프로그램이 종료됩니다.")




