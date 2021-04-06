import os
import csv
csvpath = os.path.join('Resources', 'PyBank.csv')
with open(csvpath) as fin:
    headerline = fin.next()
    total = 0
    for row in csv.reader(fin):
        total = int(row[1])
    print (total)