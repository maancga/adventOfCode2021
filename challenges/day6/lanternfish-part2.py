import sys
import utils

READING_MODE = "r"
input_file_name = sys.argv[1]
number_of_days = int(sys.argv[2])


def main():
    all_measurements = utils.get_clean_measurements_from_file(input_file_name)
    fishes = len(list(all_measurements[0].split(",")))
    current_day = 1
    n = 0
    while current_day <= number_of_days:
        if current_day % 7 == 0:
            if n < 1:
                fishes = fishes * 2
                n += 1
            else:
                fishes = fishes * 2 - n * 2
                n *= 2
        current_day += 1

    print(fishes)


main()
