num=input("숫자는? ")

while len(num)>5:
    print("99999이하의 수만 가능합니다")
    num=input("숫자는? ")

tmpnum=num
if len(tmpnum)>3:
    tmpnum=tmpnum[:len(tmpnum)-3]+","+tmpnum[len(tmpnum)-3:len(tmpnum)]
print("%s 원" % tmpnum)


kornumdic={'1':'','2':"이","3":"삼","4":"사","5":"오","6":"육","7":'칠','8':'팔','9':"구","0":" "}
kornumdic2={-5:'만',-4:'천',-3:'백',-2:'십',-1:""}
kornumword=""
if num[-1]=="1":
    kornumword="일"

else:
    kornumword=kornumdic[num[-1]]

j=-1
while -j<len(num):
    if num[j-1]=='0':
        j-=1
        continue
    else:
        kornumword=kornumdic[num[j-1]]+kornumdic2[j-1]+kornumword
    j-=1
print("%s원" % kornumword)
