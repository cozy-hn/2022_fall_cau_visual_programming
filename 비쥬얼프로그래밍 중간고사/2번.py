import string
import operator
while True:
    str_=input(">")
    str_.lower()
    list_=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    list_num=[]
    for i in list_:
        list_num.append(str_.count(i))
    dic_={ name:value for name, value in zip(list_, list_num) }
    sdict = sorted(dic_.items(), key=operator.itemgetter(1))
    print("%s : %d회" %(sdict[-1][0],sdict[-1][1]))