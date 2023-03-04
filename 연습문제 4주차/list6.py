mylist = [ [1,2], [3,4,5], [6,7,8,9], [10,11,12,13,14] ]
sum=0
for i in mylist:
    for j in i:
        sum+=j
print(sum)