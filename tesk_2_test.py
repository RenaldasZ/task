import unittest
import datetime

def calculate_color_durations(filename):
    color_durations = {'Red': datetime.timedelta(), 'Yellow': datetime.timedelta(), 'Green': datetime.timedelta()}
    
    with open(filename, 'r') as file:
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

class TestColorDurations(unittest.TestCase):
    def test_calculate_color_durations(self):
        expected_durations = {
            'Red': datetime.timedelta(seconds=20118),
            'Yellow': datetime.timedelta(seconds=36907),
            'Green': datetime.timedelta(seconds=18194)
        }
        actual_durations = calculate_color_durations('data.txt')
        self.assertEqual(expected_durations, actual_durations)

if __name__ == '__main__':
    unittest.main()
