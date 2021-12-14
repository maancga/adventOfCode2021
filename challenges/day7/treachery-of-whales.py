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
    for index, counting_crab in enumerate(crabs):
        counting_crab = int(counting_crab)
        distances = 0
        for crab in crabs:
            crab = int(crab)
            distances += index - crab if index >= crab else crab - index
        if distances < minimun_distance:
            shortestCrab = index
            minimun_distance = distances
    print(shortestCrab, minimun_distance)


main()
