"""
Task 5: Find number of lines with mistakes (multiple colours active at the same time or no colours active)

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

import os

def count_lines_with_mistakes(file_path):
    """
    Count the number of lines with mistakes in the data file.

    A line is considered to have a mistake if multiple colors are active at the same time
    or no colors are active.

    Args:
    - file_path (str): The path to the data file.

    Returns:
    - int: The number of lines with mistakes.
    """
    mistakes_count = 0

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: '{file_path}' file not found.")

    with open(file_path, 'r') as file:
        next(file)

        # Iterate through each line in the file
        line_number = 1
        for line in file:
            line_number += 1
            try:
                # Split each line into its components
                red, yellow, green, *_ = map(int, line.strip().split(',')[:3])

                # Check if multiple colors are active or no colors are active
                if (red + yellow + green) != 1:
                    mistakes_count += 1
            except (ValueError, IndexError):
                print(f"Warning: Invalid data format in line {line_number}. Skipping.")

    return mistakes_count

def main():
    file_path = 'data.txt'
    try:
        mistakes_count = count_lines_with_mistakes(file_path)
        print("Number of lines with mistakes:", mistakes_count)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
    