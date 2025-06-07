import requests
import json
import csv

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
todos_by_user = {}
for todo in todos:
    user_id = todo["userId"]
    if user_id not in todos_by_user:
        todos_by_user[user_id] = []
        todos_by_user[user_id].append(todo)
print(todos)

with open('todos.csv', 'w') as f:
    writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=todos[0].keys())
    writer.writeheader()
    for todo in todos:
        writer.writerow(todo)


