import unittest

def count_complete_cycles(filename):
    cycles_count = 0

    with open(filename, 'r') as file:
        next(file)

        prev_prev_line = list(map(int, next(file).strip().split(',')[:3]))
        prev_line = list(map(int, next(file).strip().split(',')[:3]))

        for line in file:
            red, yellow, green, *_ = map(int, line.strip().split(',')[:3])

            current_line_completes_cycle = (
                red == 0 and yellow == 1 and green == 0 and
                prev_line[0] == 1 and prev_line[1] == 0 and prev_line[2] == 0 and
                prev_prev_line[0] == 0 and prev_prev_line[1] == 1 and prev_prev_line[2] == 0
            )

            if current_line_completes_cycle:
                cycles_count += 1

            prev_prev_line = prev_line
            prev_line = [red, yellow, green]

    return cycles_count

class TestCompleteCycles(unittest.TestCase):
    def test_count_complete_cycles(self):
        # expected result
        expected_cycles_count = 3263
        # function called with the data file path
        actual_cycles_count = count_complete_cycles('data.txt')
        # actual result check
        self.assertEqual(expected_cycles_count, actual_cycles_count)

if __name__ == '__main__':
    unittest.main()

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.016s

# OK