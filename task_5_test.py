import unittest
from task_5 import count_lines_with_mistakes

class TestCountLinesWithMistakes(unittest.TestCase):
    def setUp(self):
        self.valid_file_path = 'data.txt'

    def test_count_lines_with_mistakes_valid_file(self):
        mistakes_count = count_lines_with_mistakes(self.valid_file_path)
        self.assertEqual(mistakes_count, 671)

    def test_count_lines_with_mistakes_invalid_file(self):
        invalid_file_path = 'invalid_data.txt'

        with open(self.valid_file_path, 'r') as valid_file, open(invalid_file_path, 'w') as invalid_file:

            header = valid_file.readline()
            invalid_file.write(header)

            for line_number, line in enumerate(valid_file, start=1):
                try:
                    red, yellow, green, *_ = map(int, line.strip().split(',')[:3])
                    if (red + yellow + green) != 1:
                        # Write the line to the new file if there's a mistake
                        invalid_file.write(line)
                except (ValueError, IndexError):
                    print(f"Warning: Invalid data format in line {line_number}. Skipping.")

        # Count mistakes in the new file
        mistakes_count = count_lines_with_mistakes(invalid_file_path)
        self.assertEqual(mistakes_count, 671)

if __name__ == '__main__':
    unittest.main()
