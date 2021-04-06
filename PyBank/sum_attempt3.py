import os
import csv
cr = csv.reader(open('Resources', 'PyBank.csv'))
cr.next() # to skip the header 

total = 0
for row in cr:  
   total += int(row[2])
   # possibly do other things with data/rows 

print (total)