import unittest

def count_colors(filename):
    color_counts = {'Red': 0, 'Yellow': 0, 'Green': 0}
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            red, yellow, green, *_ = map(int, line.strip().split(',')[:3])
            color_counts['Red'] += red
            color_counts['Yellow'] += yellow
            color_counts['Green'] += green
    return color_counts

class TestColorCount(unittest.TestCase):
    def test_count_colors(self):
        expected_counts = {'Red': 4020, 'Yellow': 7655, 'Green': 3996}
        actual_counts = count_colors('data.txt')
        self.assertEqual(expected_counts, actual_counts)

if __name__ == '__main__':
    unittest.main()

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.017s

# OK
