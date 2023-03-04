import sys
N=int(input("몇 단 시작? : "))
M=int(input("몇 단 종료? : "))
if(M-N>3):
    print("M-N이 조건에 위배됩니다")
    sys.exit()
if(M-N==0):
    for i in range(1,10):
        for j in range(N,M+1):
            print("                                   ",j,"x",i,"=",format(j*i, '2'),end="")
        print("                                   ")
if(M-N==1):
    for i in range(1,10):
        for j in range(N,M+1):
            print("                    ",j,"x",i,"=",format(j*i, '2'),end="")
        print("                    ")
if(M-N==2):
    for i in range(1,10):
        print(" ",end="")
        for j in range(N,M+1):
            print("            ",j,"x",i,"=",format(j*i, '2'),end="")
        print("             ")
if(M-N==3):
    for i in range(1,10):
        for j in range(N,M+1):
            print("        ",j,"x",i,"=",format(j*i, '2'),end="")
        print("        ")
    


#총 80칸 구구단 시행 한번에 10칸으로 고정
#단 1개 출력 시 35/구구단/35
#단 2개 출력 시 20/구구단/20/구구단/20
#단 3개 출력 시 13/구구단/12/구구단/12/구구단/13
#단 4개 출력 시 8/구구단/8/구구단/8/구구단/8/구구단/8
#단 5개 이상 출력 명령 시 종료
