"""
Task 2: Find how long each color was active for.

This script reads data from a file and calculates the total duration
of each color (Red, Yellow, and Green) being active. It then prints
the calculated durations for each color.

Input:
- The data file 'data.txt' containing comma-separated values representing
  the occurrences of each color and their corresponding active durations.

Output:
- Total duration of each color (Red, Yellow, Green) being active printed to the console.
"""

import datetime

# Store the total duration of each color
color_durations = {'Red': datetime.timedelta(), 'Yellow': datetime.timedelta(), 'Green': datetime.timedelta()}

# Open the data file
with open('data.txt', 'r') as file:
    next(file)
    # Iterate through each line in the file
    for line in file:
        # Split each line into its components
        red, yellow, green, time_active_str, *_ = line.strip().split(',')
        time_active = datetime.timedelta(seconds=int(time_active_str))
        
        # Update the duration for each color
        if int(red):
            color_durations['Red'] += time_active
        elif int(yellow):
            color_durations['Yellow'] += time_active
        elif int(green):
            color_durations['Green'] += time_active

for color, duration in color_durations.items():
    print(f"{color}={duration}")