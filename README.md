## Task 1 Find the number of red, yellow & green occurrences.

We use the dictionary to store and update the counts for each color.
The loop directly updates the counts in the dictionary.
We access the counts from the dictionary using the respective keys ('Red', 'Yellow', 'Green').

Output: 

`Red=4020, Yellow=7655, Green=3996`


## Task 2: Find how long each colour was active for.

The script uses a dictionary to store and update the total duration
for each color. It iterates through each line in the file, extracts
the color and its corresponding active time, and updates the duration
for the respective color in the dictionary.

Output:

`Red=5:35:18, Yellow=10:15:07, Green=5:03:14`


## Task 3: Extract and save all times when the Green signal was active from a data file.

The script reads data from a file and extracts all the times when the Green
signal was active. It then saves these times to a file named `'green_active_times.txt'`.
If no times when the Green signal was active are found, it prints a message indicating
that.

p.s.
Since the script doesn't contain any complex logic that needs to be tested in isolation, testing it might not provide significant value.

Output:

`Green was active 3996 times. Green Timings are saved in green_active_times.txt file`


