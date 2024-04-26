"""
Count the occurrences of red, yellow, and green in the data file.

This script reads data from a file and counts the occurrences of each color
(Red, Yellow, and Green). It then prints the counts for each color.

"""

# Initialize counters for each color
color_counts = {'Red': 0, 'Yellow': 0, 'Green': 0}

# Open the data file
with open('data.txt', 'r') as file:
    next(file)
    # Iterate through each line in the file
    for line in file:
        # Split each line into its components
        red, yellow, green, *_ = map(int, line.strip().split(',')[:3])
        # Update the counters
        color_counts['Red'] += red
        color_counts['Yellow'] += yellow
        color_counts['Green'] += green

print("Red={}, Yellow={}, Green={}".format(color_counts['Red'], color_counts['Yellow'], color_counts['Green']))
