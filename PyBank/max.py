import csv
import os
csvpath = os.path.join('Resources', 'PyBank.csv')
csvreader = csv.reader(csvpath, delimiter=',')
next(csvreader)
answer = max(int(column[1].replace(',', '')) for column in csvreader)
print (answer)