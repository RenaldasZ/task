import pandas as pd
import datetime

def main():
    file_path = 'data.txt'
    try:
        # Read data using Pandas
        data = pd.read_csv(file_path)

        # Calculate color durations
        color_durations = data.groupby(['Red', 'Yellow', 'Green'])['TimeActive'].sum()

        # Print the total duration of each color being active
        for index, duration in color_durations.items():
            colors = [color for color, value in zip(['Red', 'Yellow', 'Green'], index) if value == 1]
            print(f"{' & '.join(colors)}={datetime.timedelta(seconds=duration)}")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
