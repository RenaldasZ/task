"""
Task 4: Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data.

This script reads data from a file and counts the number of complete cycles,
where a cycle is defined as the sequence: Red-Yellow-Green-Yellow-Red.

Algorithm:
1. It initializes two variables to count correct and incorrect cycles.
2. Opens the data file.
3. Skips the header line.
4. Reads the first two lines to initialize the previous colors.
5. Iterates through the rest of the lines:
   a. Splits each line into its components (Red, Yellow, Green).
   b. Checks if the current line completes the cycle by comparing colors with previous lines.
   c. If the current line completes the cycle, it increments the correct cycle count, otherwise increments the incorrect cycle count.
   d. Updates the previous lines for the next iteration.
6. Prints the total number of correct and incorrect cycles.

"""

import os

def count_cycles(file_path):
    """
    Count the number of correct and incorrect cycles in the data file.

    Args:
    - file_path (str): The path to the data file.

    Returns:
    - tuple: A tuple containing the counts of correct cycles and incorrect cycles.
    """
    correct_cycles_count = 0
    incorrect_cycles_count = 0

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: '{file_path}' file not found.")

    with open(file_path, 'r') as file:
        next(file)  # Skip header
        try:
            # Read the first two lines to initialize the previous colors
            _, _, prev_prev_green = map(int, next(file).strip().split(',')[:3])
            _, _, prev_green = map(int, next(file).strip().split(',')[:3])

            # Iterate through the rest of the lines
            for line in file:
                try:
                    # Split each line into its components
                    _, _, current_green, *_ = map(int, line.strip().split(',')[:3])

                    # Check if the current line completes the cycle
                    if prev_prev_green == 0 and prev_green == 1 and current_green == 0:
                        correct_cycles_count += 1
                    else:
                        incorrect_cycles_count += 1

                    # Update the previous colors for the next iteration
                    prev_prev_green = prev_green
                    prev_green = current_green

                except (ValueError, IndexError):
                    # Handle exceptions that may occur due to invalid or incomplete lines
                    print("Warning: Skipping invalid line.")

        except FileNotFoundError as e:
            print(e)

    return correct_cycles_count, incorrect_cycles_count

def main():
    file_path = 'data.txt'
    try:
        correct_cycles_count, incorrect_cycles_count = count_cycles(file_path)
        print("Number of correct cycles: ", correct_cycles_count)
        print("Number of incorrect cycles: ", incorrect_cycles_count)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
