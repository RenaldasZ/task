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

import os
import datetime

def calculate_color_durations(file_path):
    """
    Calculate the total duration of each color being active.

    Args:
    - file_path (str): The path to the data file.

    Returns:
    - dict: A dictionary containing the total duration of each color.
    """
    color_durations = {'Red': datetime.timedelta(), 'Yellow': datetime.timedelta(), 'Green': datetime.timedelta()}

    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' file not found or it is corrupted.")
        return color_durations

    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            red, yellow, green, time_active_str, *_ = line.strip().split(',')
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
    color_durations = calculate_color_durations(file_path)
    print_color_durations(color_durations)

if __name__ == "__main__":
    main()