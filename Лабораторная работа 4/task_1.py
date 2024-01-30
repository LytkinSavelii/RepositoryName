# TODO решите задачу
import json


def task(name):
    with open(name) as json_file:
        data = json.load(json_file)
    products_sum = round(sum(item.get("score", 0) * item.get("weight", 0) for item in data), 3)
    return products_sum

res = task("input.json")
print(res)


print(task())
