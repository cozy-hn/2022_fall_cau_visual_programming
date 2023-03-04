equation=input("수식을 입력하세요 : ")
num=0
numed=0
numlist=[]
for i in equation:
    if(i=="+" or i=="-"):
        numlist.append(equation[numed:num])
        numed=num
    num+=1
numlist.append(equation[numed:]) #수식상 맨 마지막 항이 남아서 따로 넣어줌
sum=0
for i in numlist:
    sum=sum+int(i)
print("= %d" % sum)
