# Create a Python script that analyzes the votes and calculates each of the following:
#  -The total number of votes cast
#  -A complete list of candidates who received votes
#  -The percentage of votes each candidate won
#  -The total number of votes each candidate won
#  -The winner of the election based on popular vote


# Import dependencies
import os
import csv

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))


# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("Resources", "book1.csv")

#Define variables
total_votes=0

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
 
    # Read the header row first
    csv_header = next(csvfile)

    for row in csv_reader:  
        total_votes = total_votes + 1

print(f"Total votes: {total_votes}")