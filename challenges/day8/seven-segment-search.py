import sys
import utils


READING_MODE = "r"
input_file_name = sys.argv[1]


def main():
    all_measurements = utils.get_clean_measurements_from_file(input_file_name)
    measurements_splited = []
    for measurement in all_measurements:
        entry, output = measurement.split("|")
        measurements_splited.append([entry, output])
    count_unique_codes = 0
    UNIQUE_SEGMENTS = {2, 4, 3, 7}
    for measurement in measurements_splited:
        for word in measurement[1].split(" "):
            if len(word) in UNIQUE_SEGMENTS:
                print(word)
                count_unique_codes += 1
    print(count_unique_codes)


main()
