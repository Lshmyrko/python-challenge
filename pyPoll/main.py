import csv

# Initialize a variable to store the count of months
total_votes = 0

# Open the CSV file
with open('election_data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Loop through each row in the CSV file
    for row in csv_reader:
        total_votes += 1  # Increment the total count for each row

# Print the total number of votes
print("Total number of votes:", total_votes)



import csv

# Initialize a dictionary to store candidate vote counts
candidate_votes= {}

# Initialize a variable to store the total number of votes
total_votes = 0

# Open the CSV file
with open('election_data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Loop through each row in the CSV file
    for row in csv_reader:
        total_votes += 1  # Increment the total count for each row
        candidate = row['Candidate']  # Assuming 'Candidate' is the column header for candidate names

        # Update the vote count for the candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate and print the percentage of votes for each candidate
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.2f}% ({votes})")
print("-------------------------")

# Find and print the winner
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print("-------------------------")


