#! usr/bin/env python3
"""Program calculates average 10k run time based off user input."""

def main():
    """Runs program."""
    run_timing()

def run_timing():
    """Calculates average 10km run time based off user input."""
    number_of_runs = 0
    total_run_time = 0.0

    while True:
        current_run_time = input("Enter 10km run time: ")
        if current_run_time:
            number_of_runs += 1
            total_run_time += int(current_run_time)
        else:
            break


    print(f"Average of {total_run_time / number_of_runs}, over {number_of_runs} runs")


if __name__ == '__main__':
    main()
