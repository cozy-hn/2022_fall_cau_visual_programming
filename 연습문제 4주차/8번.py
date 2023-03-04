time=int(input("초= "))
hour=time//3600
print("%d시간" %hour)
time-=(3600*hour)

minu=time//60
print("%d분" %minu)
time-=(60*minu)

print("%d초" %time)
