import requests
import json

client = {"job": "management", "duration": 400, "poutcome": "success"}


url = 'http://localhost:9696/predict'
response = requests.post(url, json=client)
result = response.json()

print(json.dumps(result, indent=2))