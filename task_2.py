"""
Task 2: Find how long each color was active for.

This script reads data from a file and calculates the total duration
of each color (Red, Yellow, and Green) being active. It then prints
the calculated durations for each color.

Input:
- The data file 'data.txt' containing comma-separated values representing
  the occurrences of each color and their corresponding active durations.

Output:
- Total duration of each color (Red, Yellow, Green) being active printed to the console.
"""

import datetime

def read_color_data(file_path):
    """
    Read color data from the file.

    Args:
    - file_path (str): The path to the data file.

    Returns:
    - list: A list of tuples containing color data.
    """
    color_data = []

    try:
        with open(file_path, 'r') as file:
            next(file)
            for line in file:
                color_data.append(line.strip().split(','))
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: '{file_path}' file not found or it is corrupted.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the file: {e}")

    return color_data

def calculate_color_durations(color_data):
    """
    Calculate the total duration of each color being active.

    Args:
    - color_data (list): A list of tuples containing color data.

    Returns:
    - dict: A dictionary containing the total duration of each color.
    """
    color_durations = {'Red': datetime.timedelta(), 'Yellow': datetime.timedelta(), 'Green': datetime.timedelta()}

    for red, yellow, green, time_active_str, *_ in color_data:
        time_active = datetime.timedelta(seconds=int(time_active_str))
        
        if int(red):
            color_durations['Red'] += time_active
        elif int(yellow):
            color_durations['Yellow'] += time_active
        elif int(green):
            color_durations['Green'] += time_active

    return color_durations

def print_color_durations(color_durations):
    """
    Print the total duration of each color being active.

    Args:
    - color_durations (dict): A dictionary containing the total duration of each color.
    """
    for color, duration in color_durations.items():
        print(f"{color}={duration}")

def main():
    file_path = 'data.txt'
    try:
        color_data = read_color_data(file_path)
        color_durations = calculate_color_durations(color_data)
        print_color_durations(color_durations)
    except FileNotFoundError as e:
        print(e)
    except RuntimeError as e:
        print(e)

if __name__ == "__main__":
    main()
