import json
import requests
import pandas as pd

header = {'Content-Type': 'application/json', 'Accept': 'application/json'}

test_df = pd.read_csv('test_data/test_df.csv', encoding="utf-8-sig")
test_y = pd.read_csv('test_data/test_y.csv', encoding="utf-8-sig")

data = test_df.to_json(orient='records')
resp = requests.post("http://172.17.0.2:5000/predict", data=json.dumps(data), headers=header)

print(resp.status_code)
print(resp.json())
