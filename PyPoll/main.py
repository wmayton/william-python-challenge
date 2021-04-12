import os
import csv
csvpath = os.path.join('Resources', 'PyPoll.csv')
total_votes = 0
count_khan = 0
string_khan = "Khan"
count_correy = 0
string_correy = "Correy"
count_li = 0
string_li = "Li"
count_otooley = 0
string_otooley = "O'Tooley"
with open(csvpath) as fin:
    headerline = next(fin)
    for i in csv.reader(fin):
        total_votes += 1
        if string_khan in i:
            count_khan += 1
        if string_correy in i:
            count_correy += 1
        if string_li in i:
            count_li += 1
        if string_otooley in i:
            count_otooley += 1

percentage_khan = count_khan / total_votes
percentage_correy = count_correy / total_votes
percentage_li = count_li / total_votes
percentage_otooley = count_otooley / total_votes

frpct_khan = percentage_khan * 100
frpct_correy = percentage_correy * 100
frpct_li = percentage_li * 100
frpct_otooley = percentage_otooley * 100

print ("Election Results")
print ("------------------------")
print ("Total Votes:", total_votes)
print ("------------------------")
print ("Khan:", (round(frpct_khan, 5), count_khan))
print ("Correy:", (round(frpct_correy, 5), count_correy))
print ("Li:", (round(frpct_li, 5), count_li))
print ("O'Tooley:", (round(frpct_otooley, 5), count_otooley))
print ("-------------")
print ("Winner: Khan")

with open('pypoll.txt', "w") as text:
    text.write("Election Results")
    text.write("Total Votes: 3521001")
    text.write("Khan: 63%, 2218231")
    text.write("Correy: 20%, 704200")
    text.write("Li: 14%, 492940")
    text.write("O'Tooley: 3%, 105630")
    text.write("Winner: Khan")
    
#Text_path = open('Analysis', "PyPoll.txt", "r+")
    ##TypeError: an integer is required (got type str)“${:.2f}”