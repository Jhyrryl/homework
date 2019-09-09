import os
import csv

# initialize data collection variables
net_total = 0
change_total = 0
month_count = 0
first_month = None
last_month = None

prev_amount = None
max_incr_amt = None
max_incr_month = None
max_decr_amt = None
max_decr_month = None

# create a path to our data
data_path = os.path.join('.', 'Resources', 'budget_data.csv')

# open and read in the data
with open(data_path, newline='') as budget_file:
	budget_data = csv.reader(budget_file, delimiter=',')

	# data has a header, so pull it before looping on the rest
	header = next(budget_data)

	# loop through and analyze the data
	for row in budget_data:
		month_count += 1

		# track net total amounts
		amount = int(row[1])
		net_total += amount

		if month_count == 1:
			# there is no "change" for the first month of data
			# but we can use the first month to label our results
			first_month = row[0]
		else:
			# calculate monthly change and track total
			change = amount - prev_amount
			change_total += change

			if change > 0:
				# check for a new max increase
				if (max_incr_amt == None) or (amount > max_incr_amt):
					max_incr_amt = change
					max_incr_month = row[0]
			elif change < 0:
				# check for a new max decrease
				if (max_decr_amt == None) or (amount < max_decr_amt):
					max_decr_amt = change
					max_decr_month = row[0]

			# find last month for results label
			last_month = row[0]

		# store current amount for next iteration's calculation
		prev_amount = amount

# calculate average change
average_change = change_total / (month_count - 1)

# create unique label for the results, based on dates
date_range = f"{first_month}_{last_month}"

# build result strings
analysis = []
analysis.append(f"\nFinancial Analysis -- {date_range}")
analysis.append("---------------------------------------")
analysis.append(f"Total Months: {month_count}")
analysis.append(f"Total: ${net_total}")
analysis.append(f"Average Change: ${average_change:0.2f}")
analysis.append(f"Greatest Increase in Profits: {max_incr_month} (${max_incr_amt})")
analysis.append(f"Greatest Decrease in Profits: {max_decr_month} (${max_decr_amt})")

# output the results to terminal and a text file
out_path = os.path.join('.', "Output", f"{date_range}.txt")
with open(out_path, 'w') as out:
	for entry in analysis:
		print(entry)
		out.write(entry + '\n')
