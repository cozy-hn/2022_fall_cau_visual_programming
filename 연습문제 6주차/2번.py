refrigerator = {0, 1, 2, 3, 4, 5, 6}
listref=list(refrigerator)
refdic={"달걀":0,"양파":1,"당근":2,"감자":3,"두부":4,"버섯":5,"소고기":6,"참기름":7,"미역":8,"버섯":9}
reversrefdic={v:k for k,v in refdic.items()}
# (0: 달걀, 1: 양파, 2: 당근, 3: 감자, 4: 두부, 5: 버섯, 6:소고기, 7: 참기름, 8: 미역, 9: 버섯)
str1=input()
list1=list(str1.split())
set1=set()
for i in list1:
    set1.add(refdic[i])
nothaveset=(set1-refrigerator)
for i in nothaveset:
    print("%s " %reversrefdic[i],end="")
        
