"""
Task 3: Find all times when Green was active (by time)

This script reads data from a file and extracts all the times when the Green
signal was active. It then saves these times to a file named 'green_active_times.txt'.
If no times when the Green signal was active are found, it prints a message indicating
that.

Input:
- The data file 'data.txt' containing comma-separated values representing
  the occurrences of each color, their corresponding active durations,
  and the time of each occurrence.

Output:
- A file named 'green_active_times.txt' containing all the times when
  the Green signal was active. If no such times are found, a message
  indicating that is printed to the console.
"""

import os
import datetime

def find_green_active_times(file_path):
    """
    Find all times when the Green signal was active from the data file.

    Args:
    - file_path (str): The path to the data file.

    Returns:
    - list: A list containing all the times when the Green signal was active.
    """
    green_times = []

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: '{file_path}' file not found.")

    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            _, _, green, _, time_str = map(str.strip, line.split(','))
            if int(green):
                time = datetime.datetime.strptime(time_str, '%H:%M:%S').time()
                green_times.append(time)

    return green_times

def save_green_active_times(green_times, output_file_path='green_active_times.txt'):
    """
    Save all times when the Green signal was active to a file.

    Args:
    - green_times (list): A list containing all the times when the Green signal was active.
    - output_file_path (str): The path to the output file (default is 'green_active_times.txt').
    """
    with open(output_file_path, 'w') as output_file:
        for time in green_times:
            output_file.write(str(time) + '\n')
    print("Times when Green was active saved to", output_file_path)

def main():
    file_path = 'data.txt'
    try:
        green_times = find_green_active_times(file_path)
        for time in green_times:
          print(time)
          
        if green_times:
            save_green_active_times(green_times)
        else:
            print("No times when Green was active found in the data.")
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
