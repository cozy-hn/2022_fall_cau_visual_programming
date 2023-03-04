import json
with open('seoul.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)
sum_=0
for i in json_data["DATA"]:
    if i["jcg_dt"][:7]=='2022.12':
        sum_+=int(i["jongnoadd"])
print(sum_)