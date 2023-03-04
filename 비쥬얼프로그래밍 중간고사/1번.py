import random
import string
_LENGTH=4
string_pool = string.ascii_uppercase
result=""
listtmp=[]
liststudent=[]
for i in range(300):
    for i in range(_LENGTH):
        result+=random.choice(string_pool)
    listtmp.append(result)
    result=""
    listtmp.append(random.randint(0,100))
    listtmp.append(random.randint(0,100))
    listtmp.append(random.randint(0,100))
    sum_=(listtmp[1]+listtmp[2]+listtmp[3])
    listtmp.append(sum_)
    liststudent.append(listtmp)
    listtmp=[]
liststudent.sort(key=lambda x:-x[4])
for i in range(10):
    print(liststudent[i][0],end=" ")
    print("%3d" %liststudent[i][1],end=" ")
    print("%3d" %liststudent[i][2],end=" ")
    print("%3d" %liststudent[i][3],end=" ")
    print("%3d" %liststudent[i][4],end=" ")
    print("")
    
    
    