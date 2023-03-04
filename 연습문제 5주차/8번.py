while True:
    time=int(input(("초를 입력하세요 : ")))
    if(time==0):
        break
    # 60 60**2 60**3 60**3*24 60**3*24*30 60**3*24*30*12
    if(time>=(60**2)*24*365):
        year=time//((60**2)*24*365)
        time-=(year*(60**2)*24*365)
        print("%d년" %year)
    if(time>=60**2*24*30):
        month=time//(60**2*24*30)
        time-=(month*60**2*24*30)
        print("%d월" %month)
    if(time>=60**2*24):
        day=time//(60**2*24)
        time-=(day*60**2*24)
        print("%d일" %day)
    if(time>=60**2):
        day=time//(60**2)
        time-=(day*60**2)
        print("%d시간" %day)