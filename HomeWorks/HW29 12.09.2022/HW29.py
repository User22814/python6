import requests
import json
import openpyxl


# Task 2
class Todo:
    def __init__(self, userId: int, id: int, title: str, completed: bool):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

    def get_userId(self):
        return self.userId

    def __str__(self):
        return 'UserId: {}, Id: {}, Title: {}, Completed: {}'.format(self.userId, self.id, self.title, self.completed)

    def save(self, filename: str):
        file_class = open(filename, 'w')
        file_class.write(f'UserId: {self.userId} Id: {self.id} Title: {self.title} Completed: {self.completed}')
        file_class.close()


# Task 1
def get_data():
    url = "https://jsonplaceholder.typicode.com/todos/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    data = requests.get(url=url, headers=headers, timeout=5.0)
    todos_data = data.json()
    return todos_data


todos = get_data()
# print(todos)
todos_arr = []
# print(type(todos[0]))

for todo in todos:
    elem = Todo(**todo)
    todos_arr.append(elem)

# print(todos_arr[0])

# Task 3
for i in range(len(todos_arr)):
    file = open(f'file_{i}.json', 'w')
    class_dict = {
        "userId": todos_arr[i].userId,
        'id': todos_arr[i].id,
        'title': todos_arr[i].title,
        'completed': todos_arr[i].completed
    }
    json.dump(class_dict, fp=file)
    file.close()

# Task 4
todos_task4 =[]
for i in range(len(todos_arr)):
    file = open(f'file_{i}.json', 'r')
    tmp = json.load(file)
    todos_task4.append(tmp)

# print(type(todos_task4[0]))
# print(todos_task4[0])

# Task 5
workbook = openpyxl.Workbook()
worksheet = workbook.active
counter = 1
for todo in todos_task4:
    worksheet[f"A{counter}"] = todo["userId"]
    worksheet[f"B{counter}"] = todo["id"]
    worksheet[f"C{counter}"] = todo['title']
    worksheet[f"D{counter}"] = todo["completed"]
    counter += 1
workbook.save("new.xlsx")
workbook.close()



