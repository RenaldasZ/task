"""
Extract and save all times when the Green signal was active from a data file.

This script reads data from a file and extracts all the times when the Green
signal was active. It then saves these times to a file named 'green_active_times.txt'.
If no times when the Green signal was active are found, it prints a message indicating
that.

"""

import datetime

# Store all times when Green was active
green_times = []

with open('data.txt', 'r') as file:
    next(file)
    for line in file:
        # Split each line into its components
        red, yellow, green, time_active_str, time_str = line.strip().split(',')
        # Convert time_active_str to int to check if Green was active
        if int(green):
            # Extract time from the time_str
            time = datetime.datetime.strptime(time_str, '%H:%M:%S').time()
            # Append the time to green_times list
            green_times.append(time)

# Save all times when Green was active to a file
if green_times:
    with open('green_active_times.txt', 'w') as output_file:
        for time in green_times:
            output_file.write(str(time) + '\n')

    # Prints all times when Green was active to terminal
    print("Times when Green was active:")
    for time in green_times:
        print(time)
else:
    print("No times when Green was active found in the data.")