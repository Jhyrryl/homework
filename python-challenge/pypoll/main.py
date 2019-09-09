import os
import csv

# key constants
VOTES = 'votes'
PERC = 'perc'

# initialize data collection variables
total_votes = 0
candidates = {}

# create a path to our data
data_path = os.path.join('.', 'Resources', 'election_data.csv')

# open and read in the data
with open(data_path, newline='') as election_file:
	election_data = csv.reader(election_file, delimiter=',')

	# data has a header, so pull it before looping on the rest
	header = next(election_data)

	# loop through and analyze the data
	for row in election_data:
		total_votes += 1

		name = row[2]
		if name in candidates:
			candidates[name][VOTES] += 1
		else:
			candidates[name] = {}
			candidates[name][VOTES] = 1

# process results
winners = None
win_amount = 0
for name, data in candidates.items():
	# calculate the candidate's percentage of votes
	data[PERC] = data[VOTES] / total_votes * 100

	# track current winner
	if winners == None:
		winners = [name]
		win_amount = data[VOTES]
	else:
		if data[VOTES] > win_amount:
			# new winner, so forget previous winners
			winners.clear()

		if data[VOTES] >= win_amount:
			# track tied votes with the current winner
			winners.append(name)


def line(analysis):
	analysis.append("--------------------------------")

# build result strings
analysis = []
analysis.append(f"\nElection Results")
line(analysis)
analysis.append(f"Total Votes: {total_votes}")
line(analysis)
for name, data in candidates.items():
	analysis.append(f"{name}: {data[PERC]:0.3f}% ({data[VOTES]})")
line(analysis)
if len(winners) == 1:
	analysis.append(f"Winner: {winners[0]}")
else:
	analysis.append("It's a tie!")
	analysis.append(f"Winners: ${', '.join(winners)}")
line(analysis)

# output the results to terminal and a text file
out_path = os.path.join('.', "Output", "results.txt")
with open(out_path, 'w') as out:
	for entry in analysis:
		print(entry)
		out.write(entry + '\n')

