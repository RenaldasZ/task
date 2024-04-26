"""
Calculate and print the total duration of each color from the data file.

This script reads data from a file and calculates the total duration
of each color (Red, Yellow, and Green) being active. It then prints
the calculated durations for each color.

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