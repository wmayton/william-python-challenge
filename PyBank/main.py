# import os module
import os
#import module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'PyBank.csv')
total_months = 0
with open(csvpath) as fin:
    headerline = next(fin)
    total_profit = 0
    Dates, Values = [], []
    Value_Change = 0
    for i in csv.reader(fin):
        total_months += 1
        total_profit += int(i[1])
        Dates.append(i[0])
        Values.append(int(i[1]) - Value_Change)
        Value_Change = (int(i[1]))
    Values.pop(0)
    Dates.pop(0)
    t = (sum(Values) / (total_months - 1))
    print(total_months)
    print(min(Values))
    print(max(Values))
    r = Values.index(min(Values))
    s = Values.index(max(Values))
    print(Dates[r])
    print(Dates[s])
    print(t)
    print (total_profit)





# #get max/min values for biggest profit/loss
# with open(csvpath) as csvfile:
#     data = csv.reader(csvfile, delimiter=';')
#     minVal, maxVal = [], []
#     for i in data:
#         minVal.append(i[1])
#         maxVal.append(i[2])

# print min (minVal)
# print max (maxVal)


# print ("Financial Analysis")
# print ("------------------")
# print (f"Total Months:{int(total_months)}")
# print 


# #export analysis to .txt file
# with open('PyBank.txt,' "w") as text:
#     text.write("Financial Analysis /n")
#     text.write ("---------- /n")
#     text.write (f"Total Months:{int(total_months)}"")
