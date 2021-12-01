import sys
import utils

INPUT_FILE_NAME = sys.argv[1]
READING_MODE = "r"


def main():
    measurements_file = open(INPUT_FILE_NAME, READING_MODE)
    all_measurements = measurements_file.readlines()
    all_measurements_as_int = utils.convert_string_list_to_int_list(
        all_measurements)

    previous_measurement = all_measurements_as_int[0]
    amount_of_increments = 0
    for current_measurement in all_measurements_as_int:
        if (previous_measurement < current_measurement):
            amount_of_increments += 1
        previous_measurement = current_measurement

    print(amount_of_increments)


main()
