N=int(input("N=?"))
list1=[]
cnt=0
for i in range(2,N+1):
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        list1.append(i)
    cnt=0
print(list1)
    
        
        
