import os
import csv
import collections

totalprofitloss=0
countmonths= collections.Counter()

#collect data from csv file
budgetcsv = os.path.join('resources', "budget_data.csv")

#define functions to run in the csv data file

#total months (convert to count)
def getmonths(data):
    countmonths[row[0]] += 1

#net total amount of profit/losses over the entire period
def getprofitloss(data):
    profitloss=0
    profitloss += [row[1]]
    return profitloss

#open csv file and run functions
with open(budgetcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  
    header = next(csvreader)
    
    for row in csvreader:
        getmonths(row)
        getprofitloss(row)
        
    totalprofitloss= getprofitloss() + totalprofitloss

print(f"totalmonths: {countmonths}")
print(f"totalprofitloss:{totalprofitloss}")