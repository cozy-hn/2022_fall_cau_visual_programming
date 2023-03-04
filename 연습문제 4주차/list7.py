mylist = [ 23,78,43,11,94]
tmplist=[]
mylist2=[]
tmplist.append(mylist[2])
mylist2.append(tmplist)
tmplist=[]
tmplist.append(mylist[1:4])
mylist2.append(tmplist)
tmplist=[]

tmplist.append(mylist[:])
mylist2.append(tmplist)

print(mylist2)