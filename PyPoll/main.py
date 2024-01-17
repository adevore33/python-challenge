import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

rowcount = 0
candidate_list = []
vote_count = 0
candidate_votes = {}

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)

    for row in csvreader:
        rowcount += 1
        new_candidate = (row[2])
        if new_candidate not in candidate_list:
            candidate_list.append(new_candidate)
            candidate_votes[new_candidate] = 0
        candidate_votes[new_candidate] = candidate_votes[new_candidate] + 1

charles_votes = (int(f'{candidate_votes["Charles Casper Stockham"]}'))
diana_votes = (int(f'{candidate_votes["Diana DeGette"]}'))
raymon_votes = (int(f'{candidate_votes["Raymon Anthony Doane"]}'))

percent_charles = charles_votes / rowcount
percent_diana = diana_votes / rowcount
percent_raymon = raymon_votes / rowcount

if charles_votes > diana_votes and charles_votes > raymon_votes:
    winner = 'Winner: Charles Casper Stockham'
elif diana_votes > charles_votes and diana_votes > raymon_votes:
    winner ='Winner: Diana DeGette'
elif raymon_votes > charles_votes and raymon_votes > diana_votes:
    winner ='Winner: Raymon Anthony Doane'



print("Election Results")

print("-----------------------")


print("Total Votes:", rowcount)

print("-----------------------")


print((f"Charles Casper Stockham {percent_charles: .3%}, ({charles_votes})"))
print((f"Diana DeGette  {percent_diana: .3%}, ({diana_votes})"))
print((f"Raymon Anthony Doanne  {percent_raymon: .3%}, ({raymon_votes})"))

print("-----------------------")

print(winner)
