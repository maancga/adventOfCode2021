READING_MODE = "r"
ZERO = 0


def clean_line_breaks(list_to_clean):
    for index, element in enumerate(list_to_clean):
        list_to_clean[index] = element.rstrip('\n')
    return list_to_clean


def get_clean_measurements_from_file(input_file_name):
    measurements_file = open(input_file_name, READING_MODE)
    all_measurements = measurements_file.readlines()
    return clean_line_breaks(all_measurements)


def get_length_of(element):
    return len(element)


def get_zero_value_list(size):
    return [ZERO] * size


def get_largest_number_posible_for_base(list_of_numbers, base):
    ammount_of_digits = get_length_of(
        list_of_numbers[ZERO])
    max_posible_value = (base ** ammount_of_digits) - 1
    return max_posible_value


def calculate_number_in_base(binary_filtered_list, base):
    binary_summ = 0
    digit_index = len(binary_filtered_list) - 1
    for binary_value in binary_filtered_list:
        binary_summ += int(binary_value) * base ** digit_index
        digit_index = digit_index - 1
    return binary_summ
