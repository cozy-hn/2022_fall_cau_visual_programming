phone={"홍길동":'010-4444-5555',"김중앙":'010-9191-8181','심청':"010-3232-5454"}
while True:
    namelist=list(phone.keys())
    name=input("이름>> ")
    passer=0
    for i in namelist:
        if name in i:
            print("%s    %s" % (i,phone[i]))
            passer=1
            break    
    if ((name not in namelist) and passer==0):
        if name=="add":
            newname=input("이름은? ")
            newphonenum=input("전화번호는? ")
            phone[newname]=newphonenum
            print("%s 전화번호가 추가되었습니다." % newname)
        else:
            print("찾을 수 없습니다")
        
    
    

    
