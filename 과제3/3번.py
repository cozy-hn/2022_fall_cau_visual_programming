covidf=open('owid-covid-data.csv','r')
firstline=covidf.readline()
while True:
    korline=covidf.readline()
    num=korline.find(",")
    if korline[0:num]=="KOR":
        break #한국 가장 처음까지 찾기
    
while True:
    korline=covidf.readline()
    num=korline.find(",")
    if korline[0:num]!="KOR":
        break #한국 다음 국가가 나오면 중단 ,현황이 나라순으로 정렬됨을 이용
    newestline=korline

firstlinelist=firstline.split(",")
newestlinelist=newestline.split(",")
print("한국의 코로나 최신정보")
for i in range(0,len(firstlinelist)):
    print("%s : %s" %(firstlinelist[i],newestlinelist[i]))
    
covidf.close()
    