import csv

outputlist = []
with open("course.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # print(row)
        print(type(row[0]), type(row[1]))
        outputlist.append(row)
    print(outputlist)
