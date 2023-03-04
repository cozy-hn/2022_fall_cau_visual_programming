import pickle
mylist=list(map(str,[i for i in range(1,101) if i%2==1]))
filename='pickletest.pkl'
f=open(filename,'wb')
pickle.dump(mylist,f)
f.close()
#피클 쓰기
f=open(filename,'rb')
mylistop=pickle.load(f)
print(mylistop)
f.close()
#피클 읽기