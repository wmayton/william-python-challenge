# import os module
import os
#import module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'PyBank.csv')
with open(csvpath, 'r') as file_handler:
    lines= file_handler.read()
    print(lines)
    print(type(lines))
