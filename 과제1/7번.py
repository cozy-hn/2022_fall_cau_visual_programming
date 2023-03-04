import random
rnd=user_win=com_win=user_lose=com_lose=0
print("가위바위보 게임")
print("컴퓨터 : ",com_win,"승 ",com_lose,"패,  당신 : ",user_win,"승 ",user_lose,"패",sep="")
while(user_win<3 and com_win<3):
    print("(라운드",rnd+1,")",sep="")
    rnd+=1
    computer = random.choice(["가위", "바위", "보"])
    print("컴퓨터가 결정했습니다")
    user=input("무엇을 내시겠습니까? (가위, 바위, 보) ")
    if((computer=="가위" and user=="보") or (computer=="바위" and user=="가위") or (computer=="보" and user=="바위")):
        print("컴퓨터는 ",computer,", 당신은 ",user,", 컴퓨터가 이겼습니다",sep="")
        com_win+=1
        user_lose+=1
        print("컴퓨터 : ",com_win,"승 ",com_lose,"패,  당신 : ",user_win,"승 ",user_lose,"패",sep="")
        continue
        
    if((computer=="가위" and user=="바위") or (computer=="바위" and user=="보") or (computer=="보" and user=="가위")):
        print("컴퓨터는 ",computer,", 당신은 ",user,", 당신이 이겼습니다",sep="")
        com_lose+=1
        user_win+=1
        print("컴퓨터 : ",com_win,"승 ",com_lose,"패,  당신 : ",user_win,"승 ",user_lose,"패",sep="")
        continue
        
        print("컴퓨터 : ",com_win,"승 ",com_lose,"패,  당신 : ",user_win,"승 ",user_lose,"패",sep="")
    if((computer=="가위" and user=="가위") or (computer=="바위" and user=="바위") or (computer=="보" and user=="보")):
        print("컴퓨터는 ",computer,", 당신은 ",user,", 비겼습니다",sep="")
        print("컴퓨터 : ",com_win,"승 ",com_lose,"패,  당신 : ",user_win,"승 ",user_lose,"패",sep="")
        #무승부 기록은 ppt에 안 넣었길래 출력 안했습니다.
        
