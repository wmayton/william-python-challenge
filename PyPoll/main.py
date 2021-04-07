import os
import csv
csvpath = os.path.join('Resources', 'PyPoll.csv')
total_votes = 0
with open(csvpath) as fin:
     headerline = next(fin)