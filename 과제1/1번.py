import sys
while True:
    absol=int(input("숫자를 입력하세요 "))
    if(absol==0):
        sys.exit()
    elif(absol>0):
        print(absol)
    else:
        print(-absol)

    
