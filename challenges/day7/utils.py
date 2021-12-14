READING_MODE = "r"


def clean_line_breaks(list_to_clean):
    for index, element in enumerate(list_to_clean):
        list_to_clean[index] = element.rstrip('\n')
    return list_to_clean


def get_clean_measurements_from_file(input_file_name):
    measurements_file = open(input_file_name, READING_MODE)
    all_measurements = measurements_file.readlines()
    return clean_line_breaks(all_measurements)
