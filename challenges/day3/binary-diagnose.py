import sys
import utils

INPUT_FILE_NAME = sys.argv[1]
FIRST_ELEMENT_INDEX = 0

BINARY_BASE = 2
DECIMAL_BASE = 10


def main():
    all_cleaned_measurements = utils.get_clean_measurements_from_file(
        INPUT_FILE_NAME)
    list_by_positions = count_binary_units_of_list(all_cleaned_measurements)

    binary_filtered_list = list(map(lambda position: 1
                                    if position > 0 else 0, list_by_positions))
    max_base_posible_value = utils.get_largest_number_posible_for_base(
        all_cleaned_measurements, BINARY_BASE)
    gamma_rate = utils.calculate_number_in_base(
        binary_filtered_list, BINARY_BASE)
    epsilon_rate = max_base_posible_value - gamma_rate
    print(epsilon_rate * gamma_rate)


def count_binary_units_of_list(list_to_count):
    ammount_of_digits = utils.get_length_of(
        list_to_count[FIRST_ELEMENT_INDEX])
    list_by_positions = utils.get_zero_value_list(ammount_of_digits)
    for measurement in list_to_count:
        measurement_index = 0
        for digit in measurement:
            if digit == "0":
                list_by_positions[measurement_index] -= 1
            if digit == "1":
                list_by_positions[measurement_index] += 1
            measurement_index += 1
    return list_by_positions


main()
