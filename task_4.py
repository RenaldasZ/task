"""
Count the number of complete cycles in the data.

This script reads data from a file and counts the number of complete cycles,
where a cycle is defined as the sequence: Red-Yellow-Green-Yellow-Red.

Algorithm:
1. Initialize a variable to count complete cycles.
2. Open the data file.
3. Read the first two lines to initialize the previous colors.
4. Iterate through the rest of the lines:
   a. Split each line into its components (Red, Yellow, Green).
   b. Check if the current line completes the cycle by comparing colors with previous lines.
   c. If the current line completes the cycle, increment the cycle count.
   d. Update the previous lines for the next iteration.
5. Print the total number of complete cycles.

"""

# Initialize a variable to count complete cycles
cycles_count = 0

# Open the data file
with open('data.txt', 'r') as file:
    next(file)
    
    # Read the first two lines to initialize the previous colors
    prev_prev_line = list(map(int, next(file).strip().split(',')[:3]))
    prev_line = list(map(int, next(file).strip().split(',')[:3]))
    
    # Iterate through the rest of the lines
    for line in file:
        # Split each line into its components
        red, yellow, green, *_ = map(int, line.strip().split(',')[:3])
        
        # Check if the current line completes the cycle
        current_line_completes_cycle = (
            red == 0 and yellow == 1 and green == 0 and
            prev_line[0] == 1 and prev_line[1] == 0 and prev_line[2] == 0 and
            prev_prev_line[0] == 0 and prev_prev_line[1] == 1 and prev_prev_line[2] == 0
        )

        # If the current line completes the cycle, increment the cycle count
        if current_line_completes_cycle:
            cycles_count += 1
        
        # Update the previous lines for the next iteration
        prev_prev_line = prev_line
        prev_line = [red, yellow, green]
        print(prev_line)

print("Number of complete cycles: ", cycles_count)
