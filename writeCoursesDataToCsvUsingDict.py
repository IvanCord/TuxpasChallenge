import csv

#field names
fieldnames = ["id","course"]
#data rows of csv file
rows = [{'id': '01',
         'course': 'Algorithms'},
         {'id': '02',
         'course': 'Computer networks'}]
#writing to csv file
with open ('courses2.csv', 'w', newline='') as csvfile:
    #creating a csv writer.object to write
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)