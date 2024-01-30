# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task():
    with open(INPUT_FILENAME) as c:
        row = list(csv.DictReader(c, delimiter=",", quotechar="/n"))
        print(row)

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(row, f, indent=4)


    task()

    with open(OUTPUT_FILENAME) as output:
        for line in output:
            print(line, end="")
