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

import os

def count_color_occurrences(file_path):
    """
    Count the occurrences of each color in the data file.

    This function encapsulates the logic for reading the data file and counting the occurrences
    of each color (Red, Yellow, and Green).

    Args:
    - file_path (str): The path to the data file.

    Returns:
    - dict: A dictionary containing the counts of each color.
    """
    color_counts = {'Red': 0, 'Yellow': 0, 'Green': 0}

    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' file not found or it is corrupted.")
        return color_counts

    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            red, yellow, green, *_ = map(int, line.strip().split(',')[:3])
            color_counts['Red'] += red
            color_counts['Yellow'] += yellow
            color_counts['Green'] += green

    return color_counts

def print_color_counts(color_counts):
    """
    Print the counts of each color.

    This function encapsulates the logic for printing the counts of each color (Red, Yellow, and Green)
    to the console.

    Args:
    - color_counts (dict): A dictionary containing the counts of each color.
    """
    # Check if any color count is zero
    if 0 in color_counts.values():
        print("Warning: No data recorded for at least one color.")
        
    print("Red={}, Yellow={}, Green={}".format(color_counts['Red'], color_counts['Yellow'], color_counts['Green']))

def main():
    file_path = 'data.txt'
    color_counts = count_color_occurrences(file_path)
    print_color_counts(color_counts)

if __name__ == "__main__":
    main()