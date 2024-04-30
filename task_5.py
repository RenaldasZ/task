"""
Task 5: Find number of lines with mistakes (multiple colours active at the same time or no colours active)

This script reads data from a file and counts the number of lines where multiple colors
are active at the same time or no colors are active.

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
                continue

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
    