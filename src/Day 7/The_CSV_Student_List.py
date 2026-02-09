import csv

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[2] == "Pass":
            print(row[0])
