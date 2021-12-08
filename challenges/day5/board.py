
class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.content = [["." for columns in range(
            columns)] for row in range(rows)]

    def print_board(self):
        print("---------- Board ----------")
        for row in range(len(self.content)):
            print_line = ""
            for column in range(len(self.content[row])):
                print_line += str(self.content[row][column]) + " "

            print(print_line)
        print()

    def mark_position(self, x_component, y_component):
        self.content[x_component][y_component] = self.content[x_component][y_component] + \
            1 if self.content[x_component][y_component] != "." else 1

    def count_overlaps(self):
        overlaps = 0
        for row in range(len(self.content)):
            for column in range(len(self.content[row])):
                if (self.content[row][column] != "." and self.content[row][column] >= 2):
                    overlaps += 1
        return overlaps
