prin=int(input("원금을 입력하세요(원). "))
intr=round(float(input("금리를 입력하세요(%). ")))
#혹시 정수로 안 넣을 수도 있어서 반올림했습니다 ppt에 소숫점 안 나와있길래요.
print("원금 ", prin, "원 금리 ", intr, "% 입니다.", sep="")
print("기간     합계")
year=1
while(year<=20):
    mon=prin*(1+intr/100)**year
    print(year,"년    ",round(mon,1),sep="")
    year+=1
    
