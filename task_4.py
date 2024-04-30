"""
Task 4: Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data.

This script reads data from a file and counts the number of complete cycles,
where a cycle is defined as the sequence: Red-Yellow-Green-Yellow-Red.
"""

def read_color_data(file_path):
    """
    Read color data from a file.

    Args:
        file_path (str): The path to the file containing color data.

    Returns:
        list: A list of color sequences extracted from the file.
    """
    color_sequences = []
    current_sequence = []
    last_color = None

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Process each line to extract color sequences
    for line in lines[1:]:
        row = line.strip().split(',')
        color = 'Red' if int(row[0]) == 1 else 'Yellow' if int(row[1]) == 1 else 'Green'
        if color == last_color:
            current_sequence.append(color)
        else:
            if current_sequence:
                color_sequences.append(current_sequence)
            current_sequence = [color]
            last_color = color

    # Add the last sequence
    if current_sequence:
        color_sequences.append(current_sequence)
    # print(color_sequences)
    return color_sequences


def count_correct_cycles(color_sequences):
    """
    Count the number of correct cycles in a list of color sequences.

    Args:
        color_sequences (list): A list of color sequences.

    Returns:
        int: The number of correct cycles found.
    """
    correct_cycles = 0

    for sequence in color_sequences:
        if len(sequence) >= 2 and sequence[0] == sequence[-1]:
            correct_cycles += 1

    return correct_cycles

def main():
    file_path = 'data.txt'
    try:
        color_sequences = read_color_data(file_path)
        correct_cycles = count_correct_cycles(color_sequences)
        print("Number of Correct Cycles:", correct_cycles)
    except FileNotFoundError as e:
        print(f"Error: '{file_path}' file not found.")

if __name__ == "__main__":
    main()