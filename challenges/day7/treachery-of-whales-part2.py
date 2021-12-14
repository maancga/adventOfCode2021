import sys
import utils
import math


READING_MODE = "r"
input_file_name = sys.argv[1]


def main():
    all_measurements = utils.get_clean_measurements_from_file(input_file_name)
    crabs = list(all_measurements[0].split(","))
    shortestCrab = -1
    minimun_distance = math.inf
    for counting_crab_index, counting_crab in enumerate(crabs):
        counting_crab = int(counting_crab)
        total_distances = 0
        for crab in crabs:
            crab = int(crab)
            distances_to_iterate = counting_crab_index - \
                crab if counting_crab_index >= crab else crab - counting_crab_index
            current_distance = 0
            distance_summ = 0
            while(current_distance <= distances_to_iterate):
                distance_summ += current_distance
                current_distance += 1
            total_distances += distance_summ
        if total_distances < minimun_distance:
            shortestCrab = counting_crab_index
            minimun_distance = total_distances
    print(shortestCrab, minimun_distance)


main()
