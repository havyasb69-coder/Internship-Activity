#CSV  parsing Basic
import csv
with open("D:/DS_AI_Internship/src/Day 7/data.csv", "r") as file:
    reader =  csv.reader(file)
    for row in reader:
        print(row)