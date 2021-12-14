import sys
import utils


READING_MODE = "r"
input_file_name = sys.argv[1]


def findOneCharacters(measurement):
    measurement.replace("|", "")
    for word in measurement.split(" "):
        if len(word) == 2:
            return [word[0], word[1]]


def findFourCharacters(measurement, solvedCharacters):
    measurement.replace("|", "")
    for word in measurement.split(" "):
        if len(word) == 4:
            notSolvedElements = list(filter(lambda notSolved: (
                notSolved not in solvedCharacters.values()), word))
            return notSolvedElements


def findSevenCharacters(measurement, solvedCharacters):
    measurement.replace("|", "")
    for word in measurement.split(" "):
        if len(word) == 3:
            notSolvedElements = list(filter(lambda notSolved: (
                notSolved not in solvedCharacters.values()), word))
            return notSolvedElements


def findEightCharacters(measurement, solvedCharacters):
    measurement.replace("|", "")
    for word in measurement.split(" "):
        if len(word) == 7:
            notSolvedElements = list(filter(lambda notSolved: (
                notSolved not in solvedCharacters.values()), word))
            return notSolvedElements


def main():
    all_measurements = utils.get_clean_measurements_from_file(input_file_name)
    for measurement in all_measurements:
        solvedCharacters = dict()
        elementsOfOne = findOneCharacters(measurement)
        solvedCharacters["up_right"] = elementsOfOne[0]
        solvedCharacters["down_right"] = elementsOfOne[1]
        elementsOfFour = findFourCharacters(measurement, solvedCharacters)
        solvedCharacters["center"] = elementsOfFour[0]
        solvedCharacters["up_left"] = elementsOfFour[1]
        elementsOfSeven = findSevenCharacters(measurement, solvedCharacters)
        solvedCharacters["up"] = elementsOfSeven[0]
        elementsOfEight = findEightCharacters(measurement, solvedCharacters)
        solvedCharacters["down"] = elementsOfEight[0]
        solvedCharacters["down_left"] = elementsOfEight[1]
        configurations = {
            solvedCharacters["up_right"] + solvedCharacters["down_right"]: 1,
            solvedCharacters["up_right"] + solvedCharacters["center"] + solvedCharacters["up"] + solvedCharacters["down"] + solvedCharacters["down_left"]: 2,
            solvedCharacters["up_right"] + solvedCharacters["down_right"] + solvedCharacters["center"] + solvedCharacters["up"] + solvedCharacters["down"]: 3,
            solvedCharacters["up_right"] + solvedCharacters["down_right"] + solvedCharacters["center"] + solvedCharacters["up_left"]: 4,
            solvedCharacters["up"] + solvedCharacters["up_left"] + solvedCharacters["down"] + solvedCharacters["center"] + solvedCharacters["down_right"]: 5,
            solvedCharacters["up"] + solvedCharacters["up_left"] + solvedCharacters["center"] + solvedCharacters["down_right"] + solvedCharacters["down_left"] + solvedCharacters["down"]: 6,
            solvedCharacters["up_right"] + solvedCharacters["down_right"] + solvedCharacters["up"]: 7,
            solvedCharacters["up_right"] + solvedCharacters["down_right"] + solvedCharacters["center"] + solvedCharacters["up_left"] + solvedCharacters["up"] + solvedCharacters["down"] + solvedCharacters["down_left"]: 8,
        }
        for measurement in all_measurements:
            for word in measurement.split("|")[1].split(" "):
                if word != "":
                    print(configurations)
                    print(configurations.get(word))


main()
