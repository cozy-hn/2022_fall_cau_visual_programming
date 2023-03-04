class Calc:
    def __init__(self,num=0):
        self.result=num
        
    def add(self,num):
        self.result+=num
        return self.result
    def minus(self,num):
        self.result-=num
        return self.result
    def setvalue(self,num):
        self.result=num
    def getvalue(self):
        return self.result
    def print(self):
        print(self.result)
        
cal1 = Calc( ) # 객체 생성
cal2 = Calc(5) # 5 를 초기화하여 객체 생성
cal1.setvalue(10) # 10 설정
cal1.add(20) # 20 더하기
cal1.minus(5) # 5 빼기
cal1.print( ) # 값 표시하기
cal2.add(cal1.getvalue( )) # cal1의 값을 cal2에 더하기
cal2.print( ) # 값 표시하기


