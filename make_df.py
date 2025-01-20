import requests
import json
import pandas as pd

url = 'http://apis.data.go.kr/1160100/service/GetFinaStatInfoService_V2/getBs_V2'
params = {
    'pageNo': 1,
    'numOfRows': 100,
    'resultType': 'json',
    'serviceKey': 'CInqflqEroMBIvwzFgjXQJmsywE6qccC7DzY9BmyjB8inNR88bJjlwr2NzkrLN5VZKyMf39GNtGDHdloYAKJWw=='
}
response = requests.get(url, params=params)

data = response.json()


#전체 데이터 json 형태 확인
# clean_data = json.dumps(data, indent=4, ensure_ascii=False)
# print(clean_data)


item = data['response']['body']['items']['item']
df= pd.DataFrame(item)
df
