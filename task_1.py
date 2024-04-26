# Find the number of red, yellow & green occurrences.

color_counts = {'Red': 0, 'Yellow': 0, 'Green': 0}

with open('data.txt', 'r') as file:
    next(file)
    # Iterate through each line in the file
    for line in file:
        # Each line splited into its components and separated by comma
        red, yellow, green, *_ = map(int, line.strip().split(',')[:3])
        # Update the counters
        color_counts['Red'] += red
        color_counts['Yellow'] += yellow
        color_counts['Green'] += green

print("Red={}, Yellow={}, Green={}".format(color_counts['Red'], color_counts['Yellow'], color_counts['Green']))
