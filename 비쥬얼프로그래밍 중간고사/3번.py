import string
def mysplit(str_, deli):
    listdeli = list(deli)
    liststr = list[str_]
    for i in listdeli:
        num=0
        for j in liststr:
            if i==j:
                liststr[num]==" " #딜리미터 모두 공백로 변환
            num+=1
    str_=''.join(liststr) #딜리미터가 모두 띄어쓰기로 바뀐 문자열
    cnt=0
    tmp=0
    split_list=[]
    for i in str_:
        if i==" ":
            i
            #슬라이싱해서 split_list 반환
        cnt+=1

    return split_list



str_=input(">")
deli=input(">>")
print(mysplit(str_, deli))