# import os module
import os
#import module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'PyBank.csv')
total_months = -1
for row in open(csvpath):
    total_months += 1
print (total_months)