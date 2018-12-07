#import data
import csv

#File location
Election_data = ("/Users/tonyv/python-challenge/pypoll/election_data.csv")

#Variables
Total_Votes = []
Khan = []
Correy = []
Li = []
O_Tooley = []
Winner = []

#open csv file in read mode
with open(csv_file_path,newline="", encoding="utf-8") as elections:

#store the .csv contents in the variable
csvreader = csv.reader(elections,delimiter=",")

#skip the header
header = next(csvreader)    

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.
print(f"Election Results")
print("---------------------------")
print("Total Votes")
print("---------------------------")
print("Khan:")
print("Correy:")
print("Li:")
print("O'Tooley:")
print("---------------------------")
print("Winner:")
print("---------------------------")

#Text File Result