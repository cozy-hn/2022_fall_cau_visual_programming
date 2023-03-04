height=float(input("키(cm)는? "))
m_height=height/100
weight=float(input("몸무게(kg)는 ? "))
bmi=weight/m_height**2
bmi=round(bmi,2) #소숫점 두번째자리까지만 출력했길래 반올림했습니다


#ppt 주어진 주소에 bmi가 29~30구간 처럼 비는 구간이 있길래 구간 수정했습니다

if(bmi>=30):
    print("BMI는 ",bmi,"로 비만입니다.", sep="")
elif(bmi>=25):
    print("BMI는 ",bmi,"로 과체중입니다.", sep="")
elif(bmi>=20):
    print("BMI는 ",bmi,"로 정상입니다.", sep="")
else:
    print("BMI는 ",bmi,"로 저체중입니다.", sep="")
