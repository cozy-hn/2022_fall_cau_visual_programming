import matplotlib.pyplot as plt

covidf=open('owid-covid-data.csv','r')
firstline=covidf.readline()
i=0
linelist=[]
while True:
    line = covidf.readline()
    if not line: break
    linelist.append(list(line.split(',')))

totallist=[]#국가,총확진자 저장    
for i in range(len(linelist)-1):
    if linelist[i][2]=='Africa' or linelist[i][2]=='Asia' or linelist[i][2]=='Europe' or linelist[i][2]=='European Union' or \
        linelist[i][2]=='High income' or linelist[i][2]=='International' or linelist[i][2]=='Low income' or  \
        linelist[i][2]=='Lower middle income' or linelist[i][2]=='North America' or linelist[i][2]=='Oceania' or \
        linelist[i][2]=='South America' or linelist[i][2]=='Upper middle income' or linelist[i][2]=='World':
            continue
    if linelist[i][2]!=linelist[i+1][2]:
        totallist.append([linelist[i][2],linelist[i][4]])
totallist.append([linelist[len(linelist)-1][2],linelist[len(linelist)-1][4]])

for i in totallist:
    if i[1]=='':
        i[1]=0        
    i[1]=int(i[1])
totallist.sort(key=lambda x :x[1], reverse=True)
totallist=totallist[0:20]#12/1일 기준 구글 순위와 일치하는 것 확인


nation = [totallist[i][0] for i in range(len(totallist))]
total_cases= [totallist[i][1] for i in range(len(totallist))]

plt.barh(nation, total_cases, height=0.4)
plt.xlabel('TOTAL CASES')
plt.ylabel('NATION')

plt.xticks(total_cases[::5],label=total_cases[::5])
plt.ticklabel_format(axis='x',useOffset=False, style='plain')

plt.show()
    