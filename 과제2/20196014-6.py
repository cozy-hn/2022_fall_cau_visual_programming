word=["apple"]
score=0
game=0
while game<10:
    print("단어(%s) : " % word[-1], end="")
    newword=input()
    while len(newword)>6 or len(newword)<3:
        print("3~6글자 단어만 입력해주세요")
        print("단어(%s) : " % word[-1], end="")
        newword=input()
    if newword in word:
        score-=1
        print("이미 나온 단어입니다. 1점 차감. 현재 점수 %d점" % score)
    elif newword[0]==word[-1][-1]:
        score+=1
        print("1점 획득. 현재 점수 %d점" % score)
        word.append(newword)
    else:
        score-=1
        print("끝말잇기가 안됩니다. 1점 차감. 현재 점수 %d점" % score)        
    game+=1