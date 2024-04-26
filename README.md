## Task 1: Find the number of red, yellow & green occurrences.

This script uses a dictionary to store and update the counts for each color. It iterates through the data file, incrementing the count for each color occurrence.

Output: `Red=4020, Yellow=7655, Green=3996`

---

## Task 2: Find how long each colour was active for.

The script calculates the total duration for each color being active. It reads each line in the data file, extracts the color and its corresponding active time, and updates the duration for each color.

Output: `Red=5:35:18, Yellow=10:15:07, Green=5:03:14`

---

## Task 3: Extract and save all times when the Green signal was active from a data file.

The script extracts all the times when the Green signal was active from the data file and saves these times to a file named `'green_active_times.txt'`. If no times when the Green signal was active are found, it prints a corresponding message.

Output: `Green was active 3996 times. Green Timings are saved in green_active_times.txt file`

---

## Task 4: Count the number of complete cycles in the data.

This script counts the number of complete cycles in the data, where a cycle is defined as the sequence: Red-Yellow-Green-Yellow-Red.

Output: `Number of complete cycles: 3263`

---

## Task 5: Count the number of lines with mistakes in the data.

The script counts the number of lines in the data where multiple colors are active at the same time or no colors are active.

Output: `Number of lines with mistakes: 671`
