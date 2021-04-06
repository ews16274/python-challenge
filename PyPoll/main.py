
# Import modules
import os
import csv
import collections
from collections import Counter

# Define PyPoll's variables
voters_candidates = []
votes_per_candidate = []

# Change directory to the directory of current python script
abspath = os.path.abspath(__file__)
pypoll = os.path.dirname(abspath)
os.chdir(pypoll)

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)


    # Read through each row of data after the header
    for row in csv_reader:

        voters_candidates.append(row[2])

    # Sort the list by default ascending order
    sorted_list = sorted(voters_candidates)

    
    # Arrange the sorted list by most common outcomes
    arrange_list = sorted_list

    #count votes per candidate in most common outcome order and append to a list
    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # calculate the percentage of votes per candidate in 3 decimal points
    for item in votes_per_candidate:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')
          
    
    
# -->>  Print the analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")


# Export a text file with the results
election_data = os.path.join("Analysis", "election_data.txt")
with open(election_data, "w") as textfile:

    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    textfile.write("-------------------------\n")
    textfile.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    textfile.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    textfile.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    textfile.write(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {votes_per_candidate[0][0][0]}\n")
    textfile.write("-------------------------\n")