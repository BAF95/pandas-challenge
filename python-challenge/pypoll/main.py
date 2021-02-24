import os
import csv
# sets source data path
filepath = "resources/Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv"
# sets output path(used at end of script)
output_path = os.path.join("..", "pypoll", "analysis", "pypoll.csv")

with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # sets total voters variable
    total_voters = 0
    # sets candidate list
    candidate_list = []
    # sets candidate id
    can_id = 0
    can1_vote_total = 0
    can2_vote_total = 0
    can3_vote_total = 0
    can4_vote_total = 0
    for row in csvreader:
        # total voters calculation
        count = 0
        count = + 1
        total_voters = total_voters + count

        # creates a candidate list by adding a name and comparing to the list to avoid duplicates
        # (if more than 4 candidates copy and paste bottom elif to can_id += 1 and change can_id to 4,
        # add another and row[2] != can_name4, then in args change can_name4 to can_name 5.
        # Repeat process for more candidates  add 1 and new args ever time
        if can_id == 0:
            candidate_list.insert(can_id, row[2])
            can_name1 = row[2]
            can_id += 1
        elif can_id == 1 and row[2] != can_name1:
            candidate_list.insert(can_id, row[2])
            can_name2 = row[2]
            can_id += 1
        elif can_id == 2 and row[2] != can_name1 and row[2] != can_name2:
            candidate_list.insert(can_id, row[2])
            can_name3 = row[2]
            can_id += 1
        elif can_id == 3 and row[2] != can_name1 and row[2] != can_name2 and row[2] != can_name3:
            candidate_list.insert(can_id, row[2])
            can_name4 = row[2]
            can_id += 1
        # with candidate list calc each vote earned
        # add more can names if there is more than 4 candidates as well as if statements

        if row[2] == can_name1:
            can1_vote_total += 1
        elif row[2] == can_name2:
            can2_vote_total += 1
        elif row[2] == can_name3:
            can3_vote_total += 1
        elif row[2] == can_name4:
            can4_vote_total += 1

        # print candidate list to determine order of variable assignment
        # assigns candidate to vote totals calculated above
        Khan_votes = can1_vote_total
        Correy_votes = can2_vote_total
        Li_votes = can3_vote_total
        Otooley_votes = can4_vote_total
        # calculate percentages
        Khan_percent = (can1_vote_total/ total_voters)*100
        Correy_percent = (can2_vote_total / total_voters) * 100
        Li_percent = (can3_vote_total / total_voters) * 100
        Otooley_percent = (can4_vote_total / total_voters) * 100
        # finding most voted candidate( add elif statement to add more candidates)
        vote_leader = Correy_votes
        if vote_leader < Li_votes:
            vote_leader = Li_votes
        elif vote_leader < Khan_votes:
            vote_leader = Khan_votes
        elif vote_leader < Otooley_votes:
            vote_leader = Otooley_votes


print("Election Results")
print("--------------------------------")
print(f"Total Votes: {total_voters}")
print("---------------------------------")
print(f"{can_name1}: {round(Khan_percent)}% ({Khan_votes})")
print(f"{can_name2}: {round(Correy_percent)}% ({Correy_votes})")
print(f"{can_name3}: {round(Li_percent)}% ({Li_votes})")
print(f"{can_name4}: {round(Otooley_percent)}% ({Otooley_votes})")


# begins writing process
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Votes', 'Khan Votes', 'Khan Percentage', 'Correy Votes', 'Correy Percentage', 'Li Votes', 'Li Percentage', "O'Tooley Votes", "O'Tooley Percentage"])

    # Write the second row(reference variables above)
    csvwriter.writerow([total_voters, Khan_votes, Khan_percent, Correy_votes, Correy_percent, Li_votes, Li_percent, Otooley_votes, Otooley_percent])