import csv

with open('budget_data.csv','r') as csv_file:
    csv_reader = csv.reader (csv_file)

    for line in csv_reader:
        print(line)



import csv

# Initialize a variable to store the count of months
total_months = 0

# Open the CSV file
with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Loop through each row in the CSV file
    for row in csv_reader:
        total_months += 1  # Increment the total count for each row

# Print the total number of months
print("Total number of months:", total_months)



import csv
# initialize the sum varible
sum_of_Profit_Losses = 0

with open('budget_data.csv','r') as csv_file:
    csv_reader = csv.reader (csv_file)

    column_index = 1
    next(csv_reader) #skip the head row

    for row in csv_reader:
   
        value = int(row[column_index])
        sum_of_Profit_Losses += value
    
print(f"the sum of Profit_Losses in the column is: {sum_of_Profit_Losses}")


import csv

# Initialize variables
total_change = 0
count = 0

# Create a list to store the changes
changes = []

with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row
    
    previous_value = None  # Initialize the previous value

    for row in csv_reader:
        profit_loss = int(row[1])  # Assuming the profit/losses are in the second column (0-based indexing)
        
        if previous_value is not None:
            change = profit_loss - previous_value
            total_change += change
            changes.append(change)
            count += 1
        
        previous_value = profit_loss

# Calculate the average change
average_change = total_change / count

print(f"Average change in profit/loss is: {average_change:.2f}")



import csv

# Initialize variables
max_increase = None
max_increase_date = None
max_decrease = None
max_decrease_date = None

with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row
    
    previous_value = None  # Initialize the previous value

    for row in csv_reader:
        date = row[0]  # Assuming the date is in the first column (0-based indexing)
        profit_loss = int(row[1])  # Assuming the profit/losses are in the second column
        
        if previous_value is not None:
            change = profit_loss - previous_value
            
            # Check for the greatest increase
            if max_increase is None or change > max_increase:
                max_increase = change
                max_increase_date = date
                
            # Check for the greatest decrease
            if max_decrease is None or change < max_decrease:
                max_decrease = change
                max_decrease_date = date
        
        previous_value = profit_loss

print(f"Greatest increase in profits was {max_increase} on {max_increase_date}.")
print(f"Greatest decrease in profits was {max_decrease} on {max_decrease_date}.")

