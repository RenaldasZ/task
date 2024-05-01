"""
Task 4: Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data.

This script reads data from a file and counts the number of complete cycles,
where a cycle is defined as the sequence: Red-Yellow-Green-Yellow-Red.
"""

def is_complete_cycle(line, next_line, next_next_line, next_next_next_line, next_next_next_next_line):
    """
    Check if a sequence of five lines represents a complete cycle pattern.

    Args:
        line (str): The first line of the sequence.
        next_line (str): The second line of the sequence.
        next_next_line (str): The third line of the sequence.
        next_next_next_line (str): The fourth line of the sequence.
        next_next_next_next_line (str): The fifth line of the sequence.

    Returns:
        bool: True if the sequence represents a complete cycle, False otherwise.
    """
    colors = line.strip().split(",")[:3]
    next_colors = next_line.strip().split(",")[:3]
    next_next_colors = next_next_line.strip().split(",")[:3]
    next_next_next_colors = next_next_next_line.strip().split(",")[:3]
    next_next_next_next_colors = next_next_next_next_line.strip().split(",")[:3]
    return (colors == ['1', '0', '0'] and
            next_colors == ['0', '1', '0'] and
            next_next_colors == ['0', '0', '1'] and
            next_next_next_colors == ['0', '1', '0'] and
            next_next_next_next_colors == ['1', '0', '0'])

with open('data.txt', 'r') as file:
    lines = file.readlines()

complete_cycles = 0
with open('completed_cycles.txt', 'w') as output_file:
    for i in range(len(lines)-4):
        if is_complete_cycle(lines[i], lines[i+1], lines[i+2], lines[i+3], lines[i+4]):
            complete_cycles += 1
            output_file.write(f"Start of complete cycle at line {i+1}:\n")
            for j in range(5):
                output_file.write(lines[i+j])
            output_file.write("\n\n")

print("Number of complete cycles Red-Yellow-Green-Yellow-Red followed by Red-Green-Yellow-Red:", complete_cycles)
