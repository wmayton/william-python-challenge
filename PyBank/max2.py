import os
import csv
csvpath = os.path.join('Resources', 'PyBank.csv')
with open(csvpath) as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    header = next(data)
    Dates, Values = [], []
    Value_Change = 0
    for i in data:
        Dates.append(i[0])
        # Values.append(i[1])
        Values.append(int(i[1]) - Value_Change)
        Value_Change = (int(i[1]))
    Values.pop(0)
    Dates.pop(0)
    t = (sum(Values) / (total_months - 1))
    print(min(Values))
    print(max(Values))
    r = Values.index(min(Values))
    s = Values.index(max(Values))
    print(Dates[r])
    print(Dates[s])
    print(t)

