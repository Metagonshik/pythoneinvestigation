import requests

result = requests.get("http://127.0.0.1:3000/api/family/0")
print(result.json())


