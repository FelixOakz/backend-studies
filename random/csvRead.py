import csv
# with is a keyword that dismisses need for closing file
with open("csvtest.csv") as file:
    contents = csv.reader(file)
    next(contents)
    for row in contents:
        print(row)