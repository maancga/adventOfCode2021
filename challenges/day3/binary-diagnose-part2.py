import sys
import utils

INPUT_FILE_NAME = sys.argv[1]

OXYGEN_RATING_OPTION = "Oxygen"
CO2_RATING_OPTION = "CO2"

BINARY_BASE = 2
DECIMAL_BASE = 10


def main():
    all_cleaned_measurements = utils.get_clean_measurements_from_file(
        INPUT_FILE_NAME)
    filtered_list_by_oxigen = filter_list_by_criteria(
        all_cleaned_measurements, OXYGEN_RATING_OPTION)
    filtered_list_by_CO2 = filter_list_by_criteria(
        all_cleaned_measurements, CO2_RATING_OPTION)

    oxygen_rating_result = utils.calculate_number_in_base(
        filtered_list_by_oxigen[0], BINARY_BASE)
    co2_rating_result = utils.calculate_number_in_base(
        filtered_list_by_CO2[0], BINARY_BASE)

    print(oxygen_rating_result * co2_rating_result)


def filter_by_digit(all_cleaned_measurements, digit, criteria):
    summ = 0
    for measurement in all_cleaned_measurements:
        if measurement[digit] == "0":
            summ -= 1
        if measurement[digit] == "1":
            summ += 1
    keep_value = 0
    if (summ == 0):
        keep_value = "1" if criteria == OXYGEN_RATING_OPTION else "0"
    else:
        keep_value = "1" if (criteria == OXYGEN_RATING_OPTION and summ > 0) or (
            criteria == CO2_RATING_OPTION and summ < 0) else "0"
    return list(filter(lambda measurement:
                       measurement[digit] == keep_value, all_cleaned_measurements))


def filter_list_by_criteria(all_cleaned_measurements, criteria):
    index = 0
    filtered_list = all_cleaned_measurements
    while (len(filtered_list) > 1):
        filtered_list = filter_by_digit(
            filtered_list, index, criteria)
        index += 1
    return filtered_list


main()
