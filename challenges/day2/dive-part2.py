import sys

INPUT_FILE_NAME = sys.argv[1]
READING_MODE = "r"
SEPARATOR = " "


class Position:
    def __init__(self, depth, horizontal_position, aim):
        self.depth = depth
        self.horizontal_position = horizontal_position
        self.aim = aim


position = Position(0, 0, 0)


def addUpUnits(position, units):
    position.aim -= int(units)


def addDownUnits(position, units):
    position.aim += int(units)


def addForwardUnits(position, units):
    position.horizontal_position += int(units)
    position.depth += int(units) * position.aim


posible_directions = {
    "up": addUpUnits,
    "down": addDownUnits,
    "forward": addForwardUnits
}


def main():
    path_plan_file = open(INPUT_FILE_NAME, READING_MODE)
    all_moves_from_path = path_plan_file.readlines()
    for move in all_moves_from_path:
        [direction, units] = move.split(SEPARATOR)
        posible_directions.get(direction)(position, units)

    print(position.depth * position.horizontal_position)


main()
