DataList=[]
print("데이터를 입력하세요(입력을 마치려면 0을 입력하세요)")
while True:
    Data=int(input())
    if(Data==0):
        break
    DataList.append(Data)
DataList.sort()
for i in DataList:
    print(i, end=" ")
print("(",len(DataList),"개)",sep="")



