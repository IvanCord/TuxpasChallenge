import csv
#field names
fields = ["id","course"]

#data rows of csv file
rows = [['01', 'Algorithms'],['02','Computer networks']]
#writing to csv file
with open ('courses.csv', 'w', newline='') as csvfile:
    #creating a csv writer.object
    coursewriter = csv.writer(csvfile)
    #writing the fields
    coursewriter.writerow(fields)
    #writing the data rows
    coursewriter.writerows(rows)