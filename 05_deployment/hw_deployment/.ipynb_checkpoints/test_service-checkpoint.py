import requests
import json

client = {"job": "student", "duration": 280, "poutcome": "failure"}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=client)
result = response.json()

print(json.dumps(result, indent=2))