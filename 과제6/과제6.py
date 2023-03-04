
import requests
import json


url = 'https://apis.data.go.kr/1480523/MetalMeasuringResultService/MetalService?serviceKey=WgDvO0q8BbK2j81aFL%2F4YDhpaMCx4eox%2Bko%2F5pWWzktIy2T3ZQpfHK%2BIxkkXkLiXgTdL5fJe7gfpgCwQ1Wdazg%3D%3D&pageNo=1&numOfRows=5000&resultType=JSON&date=202212&timecode=RH02'

response = requests.get(url,verify=False) #ssl인증오류 때문에 verify뺏습니다

contents = response.text

json_ob = json.loads(contents)

print("--------------------------------------------------------------------------------------")
print("2022년 12월의 수도권 미세먼지 속 납과 칼슘의 2시간 이동평균 데이터 가져오기")
print("--------------------------------------------------------------------------------------")

for i in json_ob['MetalService']['item']:
        if i["STATIONCODE"]==1:
            if i['ITEMCODE']=='90303':
                print("날짜 : %s " %i['SDATE'][:8])
                print("시간 : %s시"%i['SDATE'][8:10])
                print("미세먼지 속 금속 종류 : 납")
                print("농도 %f ng/m^3" %i['VALUE'])
                print()
            elif i['ITEMCODE']=='90319':
                print("날짜 : %s " %i['SDATE'][:8])
                print("시간 : %s시"%i['SDATE'][8:10])
                print("미세먼지 속 금속 종류 : 칼슘")
                print("농도 %f ng/m^3" %i['VALUE'])
                print()