"""
Task 4: Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data.

This script reads data from a file and counts the number of complete cycles,
where a cycle is defined as the sequence: Red-Yellow-Green-Yellow-Red.

Algorithm:
1. It initializes a variable to count complete cycles.
2. Opens the data file.
3. Skips the header line.
4. Reads the first two lines to initialize the previous colors.
5. Iterates through the rest of the lines:
   a. Splits each line into its components (Red, Yellow, Green).
   b. Checks if the current line completes the cycle by comparing colors with previous lines.
   c. If the current line completes the cycle, it increments the cycle count.
   d. Updates the previous lines for the next iteration.
6. Prints the total number of complete cycles.

"""

import os

def count_complete_cycles(file_path):
    """
    Count the number of complete cycles Red-Yellow-Green-Yellow-Red in the data file.

    Args:
    - file_path (str): The path to the data file.

    Returns:
    - int: The number of complete cycles found.
    """
    cycles_count = 0

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: '{file_path}' file not found.")

    with open(file_path, 'r') as file:
        next(file)
        try:
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

        except FileNotFoundError as e:
            print(e)

    return cycles_count

def main():
    file_path = 'data.txt'
    try:
        cycles_count = count_complete_cycles(file_path)
        print("Number of complete cycles: ", cycles_count)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
