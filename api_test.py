import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

if response.status_code == 200:
    data = response.json()
    print(data)
    print("Title:", data["title"])
    print("Completed:", data["completed"])
else:
    print("API call failed")