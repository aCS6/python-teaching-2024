import requests

id = 3
URL = f"https://jsonplaceholder.typicode.com/posts/{id}"

response = requests.get(URL, timeout=5)

print(response.status_code)
data = response.json()

print(data)