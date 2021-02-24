import os
import csv
# sets source data path
filepath = "resources/budget_data.csv"
# sets output path(used at end of script)
output_path = os.path.join("..", "pybank", "analysis", "pybank.csv")

with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # set count for total months
    total = 0
    # set value for total profits
    total_profits = 0
    # sets min/max value to be compared as rows are iterated
    max_val = 0
    min_val = 0
    for row in csvreader:

        # total months calculation
        count = 0
        count =+ 1
        total = total + count

        # converts profit/loss to integer for later use
        monthly_value = int(row[1])
        # calculates total profit
        total_profits = total_profits + monthly_value
        # determines max value in set by profit and stores variable
        if max_val < int(row[1]):
            max_val = int(row[1])
            max_out = row
        # determines min value in set by profit and stores variable
        if min_val > int(row[1]):
            min_val = int(row[1])
            min_out = row

    # adds up total profits
# calculates average via net profit / total months
average = total_profits / total
# prints result to terminal
print(f"Data output: Total Months:{total} ")
print(f"Net Profit:{total_profits} ")
print(f"Average Profit:{average}")
print(f"Most Profitable Month{max_out}  ")
print(f"Most Value Lost by Month: {min_out}")



# begins writing process
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Net Profit', 'Average Profit', 'Best Month', 'Best Month Profit', 'Worst Month', 'Worst Month Profit'])

    # Write the second row(reference variables above)
    csvwriter.writerow([total, total_profits, average, max_out[0], max_out[1], min_out[0], min_out[1]])
