import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

colors = ['#71797E', '#B2BEB5']
wedgeprops = {
    'edgecolor': 'black',
    'linestyle': '-',
    'linewidth': 1.0
}
fig = plt.figure(figsize=(10,10)) ## 캔버스 생성
fig.set_facecolor('white') ## 캔버스 배경색을 하얀색으로 설정

while True:
    ax = fig.add_subplot(121) ## 프레임 생성
    bx = fig.add_subplot(122) ## 프레임 생성
    ax.set_title("HOUR")
    bx.set_title("MINUITE")
    
    hour=datetime.now().hour
    Minute=datetime.now().minute
    Hlabels = [hour,None] ## 라벨
    Hfrequency = [1,300] ## 빈도
    hourangle=hour/12*360##angle
    explode = [-0.5,0] ## 튀어나오는 정도를 결정한다.
    ax.pie(Hfrequency, ## 파이차트 출력
        explode = explode,
        labels=Hlabels, ## 라벨 출력
        startangle=-hourangle+90, 
        counterclock=False ## 시계 방향으로 그린다.
        ,colors=colors,wedgeprops=wedgeprops
        )



    Mlabels = [Minute,None] ## 라벨
    Mfrequency = [1,1000] ## 빈도
    Minuteangle=Minute/60*360##angle

    
    explode = [0.05,0] ## 튀어나오는 정도를 결정한다.
    bx.pie(Mfrequency, ## 파이차트 출력
        explode = explode,
        labels=Mlabels, ## 라벨 출력
        startangle=-Minuteangle+90, 
        counterclock=False ## 시계 방향으로 그린다.
        ,colors=colors,wedgeprops=wedgeprops
        )

    
    plt.draw()
    plt.pause(60)
    plt.clf()