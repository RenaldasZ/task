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

def read_color_data(file_path):
    """
    Read color data from the file.

    Args:
    - file_path (str): The path to the data file.

    Returns:
    - list: A list containing the color data from the file.
    """
    color_data = []

    try:
        with open(file_path, 'r') as file:
            next(file)
            for line in file:
                color_data.append(map(int, line.strip().split(',')[:3]))
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: '{file_path}' file not found or it is corrupted.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the file: {e}")

    return color_data

def count_color_occurrences(color_data):
    """
    Count the occurrences of each color in the data.

    Args:
    - color_data (list): A list containing the color data.

    Returns:
    - dict: A dictionary containing the counts of each color.
    """
    color_counts = {'Red': 0, 'Yellow': 0, 'Green': 0}

    for red, yellow, green in color_data:
        color_counts['Red'] += red
        color_counts['Yellow'] += yellow
        color_counts['Green'] += green

    return color_counts

def print_color_counts(color_counts):
    """
    Print the counts of each color.

    Args:
    - color_counts (dict): A dictionary containing the counts of each color.
    """
    # Check if any color count is zero
    if 0 in color_counts.values():
        print("Warning: No data recorded for at least one color.")
        
    print("Red={}, Yellow={}, Green={}".format(color_counts['Red'], color_counts['Yellow'], color_counts['Green']))

def main():
    file_path = 'data.txt'
    try:
        color_data = read_color_data(file_path)
        color_counts = count_color_occurrences(color_data)
        print_color_counts(color_counts)
    except FileNotFoundError as e:
        print(e)
    except RuntimeError as e:
        print(e)

if __name__ == "__main__":
    main()
