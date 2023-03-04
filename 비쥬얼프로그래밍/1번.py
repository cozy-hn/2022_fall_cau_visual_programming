class Account:
    def __init__(self,name,accountnum):
        self.name=name
        self.accountnum=accountnum
        self.money=0
    def __str__(self):
        return '%s:%s:%d'%(self.name,self.accountnum,self.money)
    def deposit(self,money):
        if money<0:
            return False
        else:
            self.money+=money
            return True
    def withdraw(self,money):
        if money>self.money:
            return False
        else:
            self.money-=money
            return True
        




account1 = Account('홍길동', '1111-2222')
print(account1)
ret = account1.deposit(2000)
if ret :
    print(account1)
else :
    print('failed')
ret = account1.withdraw(500)
if ret :
    print(account1)
else :
    print('failed')
ret = account1.withdraw(5000)
if ret :
    print(account1)
else :
    print('failed')
