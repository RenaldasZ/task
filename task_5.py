"""
Task 5: Find the number of lines with mistakes in the data.

This script reads data from a file and counts the number of lines where multiple colors
are active at the same time or no colors are active.

Algorithm:
1. Initialize a variable to count lines with mistakes.
2. Open the data file.
3. Skip the header line.
4. Iterate through each line in the file:
    a. Split each line into its components (Red, Yellow, Green).
    b. Check if multiple colors are active or no colors are active.
    c. If the condition is met, increment the mistakes count.
5. Print the total number of lines with mistakes.

Example:
For a line in the data file:
1,0,1,5,0:00:05

The script will count it as a mistake because both Red and Green are active at the same time.

"""

# Initialize a variable to count lines with mistakes
mistakes_count = 0

# Open the data file
with open('data.txt', 'r') as file:
    next(file)  # Skip the header line
    
    # Iterate through each line in the file
    for line in file:
        # Split each line into its components
        red, yellow, green, *_ = map(int, line.strip().split(',')[:3])
        
        # Check if multiple colors are active or no colors are active
        if (red + yellow + green) != 1:
            mistakes_count += 1

# Print the total number of lines with mistakes
print("Number of lines with mistakes:", mistakes_count)
