import sys
import utils

READING_MODE = "r"
input_file_name = sys.argv[1]
number_of_days = int(sys.argv[2])


def main():
    all_measurements = utils.get_clean_measurements_from_file(input_file_name)
    fishes = list(all_measurements[0].split(","))
    current_day = 0
    while current_day < number_of_days:
        new_fish_list = fishes.copy()
        for index_fish, fish in enumerate(fishes):
            if fish == '0':
                new_fish_list[index_fish] = '6'
                new_fish_list.append('8')
            else:
                new_fish_list[index_fish] = str(int(fish) - 1)
        fishes = new_fish_list
        current_day += 1
    print(len(fishes))


main()
