import csv

outputlist = []
with open("course.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row)
        print(row["id"], row["course"])
        outputlist.append(row.values())
    print(outputlist)
