Sat_0301 = [(100, 98), (97, 95), (88, 90), (50, 58), (100, 100), (97, 100), (100, 98), (97, 95), (88, 90), (50, 58) ]
list1=[]
for i in Sat_0301:
    list1.append(list(i))
engscr=input()
englist=[]
englist.extend(list(map(int,engscr.split())))
for i in range(10):
    list1[i].append(englist[i])
sumlist=[]
for i in range(10):
    sumlist.append(sum(list1[i]))
print(sumlist)