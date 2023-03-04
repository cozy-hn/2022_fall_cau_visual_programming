import random
import sys

class City:#도시 클래스 생성
    def __init__(self,name,citynum,fee=600,owner="Empty",playerposition='NoOne',purchasefee=300):
        self.name=name
        self.citynum=citynum
        self.fee=fee
        self.owner=owner
        self.playerposition=playerposition
        self.purchasefee=purchasefee
    def getname(self):
        return self.name
    def getcitynum(self):
        return self.citynum
    def getfee(self):
        return self.fee
    def getowner(self):
        return self.owner
    def setowner(self,owner):
        self.owner=owner
    def getplayerposition(self):
        return self.playerposition
    def setplayerposition(self,playerposition):
        self.playerposition=playerposition
    def getpurchasefee(self):
        return self.purchasefee

    

START=City('START',0)#도시취급
START.setowner("START")#시작지점인 경우 아무일도 일어나지 않음, 따라서 미리 변경
Seoul=City('Seoul',1)
Tokyo=City('Tokyo',2)
Sydney=City('Sydney',3)
LA=City('LA',4)
Cairo=City('Cairo',5)
Phuket=City('Phuket',6)
New_delhi=City('New delhi',7)
Hanoi=City('Hanoi',8)
Paris=City('Paris',9)
#도시 객체 생성

city=[START,Seoul,Tokyo,Sydney,LA,Cairo,Phuket,New_delhi,Hanoi,Paris]#리스트를 만들어서 순서를 player의 location과 똑같이 만들었습니다.


class player:#플레이어 클래스 생성
    def __init__(self, playername, location=0, money=5000):
        self.playername=playername 
        self.location=location
        self.money=money

    def getplayername(self):
        return self.playername
    def getlocation(self):
        return self.location
    def setlocation(self,location):
        self.location=location
    def getmoney(self):
        return self.money
    def setmoney(self,money):
        self.money=money

            
p1=player('p1')
p2=player('p2')
#플레이어 객체 생성

def makedice():#주사위 굴리는 함수
    dice=random.randrange(1, 7)
    return dice

def controllor(player):#플레이어 위치 설정 함수
    num=player.getlocation()+makedice()
    if num>9:
        num-=10
    player.setlocation(num)

def gameend():#게임 종료 함수
    sys.exit(0)
        
    
def playerturn(player1,player2):#player1 차례
    
    controllor(player1)
    
    if city[player1.getlocation()].getowner()=="Empty":#빈 도시인 경우
        if player1.getmoney()>=city[player1.getlocation()].getpurchasefee():
            player1.setmoney(player1.getmoney()-city[player1.getlocation()].getpurchasefee())#도시 구매
            city[player1.getlocation()].setowner(player1.getplayername())#도시 주인 변경
            city[player1.getlocation()].setplayerposition(player1.getplayername())#도시에 있는 사람 위치 변경
            print("%s이 %s를 구매했습니다.\n"%(player1.getplayername(),city[player1.getlocation()].getname()))
            print("%s의 자산 : %d       %s의 자산 : %d\n" %(player1.getplayername(),player1.getmoney(),player2.getplayername(),player2.getmoney()))
        else:
            print("아무일도 일어나지 않았습니다.\n")
            
    elif city[player1.getlocation()].getowner()==player2.getplayername():#상대가 주인인 경우
        if player1.getmoney()>=city[player1.getlocation()].getfee():#p1이 통행료 이상의 돈을 가지고 있을때
             player1.setmoney(player1.getmoney()-city[player1.getlocation()].getfee())#p1의 돈 -600
             player2.setmoney(player2.getmoney()+city[player1.getlocation()].getfee())#p2의 돈 +600
             print("%s이 %s에 들려 %s에게 통행료를 지불하였습니다.\n"%(player1.getplayername(),city[player1.getlocation()].getname(),player2.getplayername()))
             print("%s의 자산 : %d       %s의 자산 : %d\n" %(player1.getplayername(),player1.getmoney(),player2.getplayername(),player2.getmoney()))
        else:#p1이 통행료 이하의 돈을 가지고 있을 경우
            print("%s의 자산 : %d       %s의 자산 : %d\n" %(player1.getplayername(),player1.getmoney(),player2.getplayername(),player2.getmoney()))
            print("%s가 %s에 들렸지만 자금난으로 인해 %s에게 돈을 지불할 수 없습니다.\n" %(player1.getplayername(),city[player1.getlocation()].getname(),player2.getplayername()))
            print("축하합니다! %s가 게임에서 승리하였습니다!" %player2.getplayername())
            gameend()#게임 종료
    else:
        print("아무일도 일어나지 않았습니다\n")



def gameplay(player1,player2):
    i=0
    print("\n--------------------------------------------------------------------\n")
    while(i<30):
        print("제 %d턴, %s의 턴입니다\n" %((i+1),player1.getplayername()))
        playerturn(player1,player2)
        print("제 %d턴, %s의 턴입니다\n" %((i+1),player2.getplayername()))
        playerturn(player2,player1)
        i+=1
        print("\n--------------------------------------------------------------------\n")
    print("game 종료!\n")
    if(player1.getmoney()>player2.getmoney()):
        print("%s의 자산 : %d       %s의 자산 : %d\n" %(player1.getplayername(),player1.getmoney(),player2.getplayername(),player2.getmoney()))
        print("축하합니다! %s가 게임에서 승리하였습니다!" %player1.getplayername()) 
    elif(player1.getmoney()<player2.getmoney()):
        print("%s의 자산 : %d       %s의 자산 : %d\n" %(player1.getplayername(),player1.getmoney(),player2.getplayername(),player2.getmoney()))
        print("축하합니다! %s가 게임에서 승리하였습니다!" %player2.getplayername()) 
    else:
        print("%s의 자산 : %d       %s의 자산 : %d\n" %(player1.getplayername(),player1.getmoney(),player2.getplayername(),player2.getmoney()))
        print("무승부입니다!")
    print("\n--------------------------------------------------------------------\n")
        
        
settingfirst=random.randrange(1, 3)#1이면 player 1먼저 시작, 2면 player2 시작
print("************GAME START!!************\n\n")
if settingfirst==1:
    print("p1 선입니다\n")
    gameplay(p1,p2)
else:
    print("p2 선입니다\n")
    gameplay(p2,p1)

