"""
Task 1: Find the number of red, yellow & green occurrences.

This script reads data from a file and counts the occurrences of each color
(Red, Yellow, and Green) in the data. It then prints the counts for each color.

Input:
- The data file 'data.txt' containing comma-separated values representing
  the occurrences of each color.

Output:
- Counts of each color (Red, Yellow, Green) printed to the console.
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
