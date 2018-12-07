#import csv data
import csv

#File location
Budget_file = ("/Users/tonyv/python-challenge/Pybank/budget_data.csv")

#Variables
total_months = []
total_profits = []
average_change = []

#Open csv file in read mode
with open(input_file,newline="", encoding="utf-8") as budget:

#store the contents of the .csv file in the vairable
csvreader = csv.reader(budget,delimiter=",")
header = next(csvreader)
for row in csvreader

#The total number of months included in the dataset
total_months.append(row[0])

#The total net amount of "Profit/Losses" over the entire period
total_profits(int[1]))

#The average change in "Profit/Losses" between months over the entire period
for i in range(len(total_profit)-1):
monthly_profit_change.append(total_profit[i+1]-total_profit[i])

#The greatest increase in profits (date and amount) over the entire period
max_increase_value = max(monthly_profit_change)

#The greatest decrease in losses (date and amount) over the entire period
max_decrease_value = min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months
print(f"Total)
print(f"Average Change
print(f"Greatest Increase in Profits)
print(f"Greatest Decrease in Profits)

#Text File
Text_file = Path("/Users/tonyv/python-challenge/Pybank/results.txt")
