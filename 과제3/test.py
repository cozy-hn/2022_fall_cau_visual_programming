    
from datetime import datetime
dtstart = datetime.now()
ans=input("= ")#마지막 띄어쓰기 제거
dtend=datetime.now()
timedel=dtend-dtstart
time=timedel.total_seconds() #타이핑 친 초
print(time)