# Create a Python script that analyzes the votes and calculates each of the following:
#  -The total number of votes cast
#  -A complete list of candidates who received votes
#  -The percentage of votes each candidate won
#  -The total number of votes each candidate won
#  -The winner of the election based on popular vote


# Import dependencies
import os
import csv

# Change directory to the directory of current python scrip
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")


# Open and read csv
with open(election_data_csv, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
 
    # Read the header row first
    csv_header = next(csvfile)

    candidate = []

    for row in csv_reader:
        candidate.append(row[2])

    candidate_count = [[x,candidate.count(x)] for x in set(candidate)]
    
    votes = []
    name = []
    
    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])

    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)

    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]       
            
total_votes = len(candidate)

correy_total = candidate.count('Correy')
correy_percent = int(correy_total) / int(total_votes)

o_tooley_total = candidate.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes

li_total = candidate.count('Li')
li_percent = li_total / total_votes

khan_total = candidate.count('Khan')
khan_percent = khan_total / total_votes

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_percent:.3%} ({khan_total})')
print(f'Correy: {correy_percent:.3%} ({correy_total})')
print(f'Li: {li_percent:.3%} ({li_total})')
print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})")
print(f'-------------------------')
print(f'Winner: {winner_name}')
print(f'-------------------------')

with open('PyPoll.txt', 'w') as text_file:
    print(f'Election Results', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Total Votes: {total_votes}', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Khan: {khan_percent:.3%} ({khan_total})', file=text_file)
    print(f'Correy: {correy_percent:.3%} ({correy_total})', file=text_file)
    print(f'Li: {li_percent:.3%} ({li_total})', file=text_file)
    print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})", file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Winner: {winner_name}', file=text_file)
    print(f'-------------------------', file=text_file)  