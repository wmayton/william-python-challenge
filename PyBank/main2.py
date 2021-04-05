import os
import csv
csvpath = os.path.join('Resources', 'PyBank.csv')
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvpath)
    total = sum(float(row[1]) for row in reader)
print(total)