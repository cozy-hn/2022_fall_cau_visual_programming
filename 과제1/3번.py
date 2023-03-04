while True:
    num=input("수? ")
    if(len(num)>30):
        print("30자리 이하의 정수만 입력할 수 있습니다.")
        continue
    num=int(num)
    if(num<0):
        print("대칭수가 아닙니다.")
        continue
    r_num=0
    tmp_num=num
    while(tmp_num!=0):
        digit=tmp_num%10
        r_num=r_num*10+digit
        tmp_num//=10
    if(num==r_num):
        print("대칭수 입니다.")
    else:
        print("대칭수가 아닙니다.")


        
