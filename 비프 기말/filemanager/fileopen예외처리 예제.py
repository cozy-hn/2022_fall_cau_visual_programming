filename='test.txt'
try :
    f = open(filename, 'r')
except   IOError:
    print('파일을 찾지 못했습니다')
else :
    print('파일을 찾았습니다')
# 파일읽기작업진행
    f.close()
finally :
    print(filename, '처리 완료')