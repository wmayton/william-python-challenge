import os
import csv
csvpath = os.path.join('Resources', 'PyBank.csv')
with open(csvpath) as fin:
    headerline = next(fin)
    total_profit = 0
    for row in csv.reader(fin):
        total_profit += int(row[1])
    print (total_profit)