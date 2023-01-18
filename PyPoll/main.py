import pandas as pd
# Read in the CSV file
election_data = pd.read_csv("election_data.csv")
election_data
# Calculate the total number of votes cast
total_votes = election_data["Ballot ID"].count()
total_votes
# Calculate the number of votes each candidate won
candidate_votes = election_data["Candidate"].value_counts()
candidate_votes
# Create a list of candidates who received votes
candidates = election_data["Candidate"].unique()
candidates
# Calculate the percentage of votes each candidate won
candidate_percentages = candidate_votes / total_votes
candidate_percentages
# Find the winner of the election based on popular vote
winner = candidate_votes.idxmax()
winner
# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3%} ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")









