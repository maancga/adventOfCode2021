
class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.content = [[BingoNumber(0) for columns in range(
            columns)] for row in range(rows)]
        self.already_won = False

    def print_board(self):
        print("---------- Board ----------")
        for row in range(len(self.content)):
            print_line = ""
            for column in range(len(self.content[row])):
                print_line += str(self.content[row][column].value) + " "

            print(print_line)
        print()

    def print_marked_values(self):
        for row in range(len(self.content)):
            print_line = ""
            for column in range(len(self.content[row])):
                if self.content[row][column].checked:
                    print_line += str(self.content[row][column].value) + " "
            print(print_line)
        print()

    def print_unmarked_values(self):
        for row in range(len(self.content)):
            print_line = ""
            for column in range(len(self.content[row])):
                if not self.content[row][column].checked:
                    print_line += str(self.content[row][column].value) + " "
            print(print_line)
        print()

    def mark_number_if_exists(self, number):
        for row in range(len(self.content)):
            for column in range(len(self.content[row])):
                self.content[row][column].checked = True if (
                    self.content[row][column].value == number) else self.content[row][column].checked

    def check_if_any_row_is_complete(self):
        for row in range(len(self.content)):
            summ_of_corrects = 0
            return_list = []
            for column in range(len(self.content[row])):
                if self.content[row][column].checked:
                    summ_of_corrects += 1
                    return_list.insert(
                        len(return_list), self.content[row][column].value)
                else:
                    break

            if (summ_of_corrects == self.columns):
                self.already_won = True
                return return_list
        return False

    def check_if_any_column_is_complete(self):
        for column in range(self.columns):
            summ_of_corrects = 0
            return_list = []
            for row in range(len(self.content)):
                if self.content[row][column].checked:
                    summ_of_corrects += 1
                    return_list.insert(
                        len(return_list), self.content[row][column].value)
                else:
                    break

            if (summ_of_corrects == self.rows):
                self.already_won = True
                return return_list
        return False

    def summ_of_none_marked(self):
        summ = 0
        for row in range(len(self.content)):
            for column in range(len(self.content[row])):
                summ += self.content[row][column].value if not(
                    self.content[row][column].checked) else 0
        return summ

    def is_complete(self):
        return self.already_won


class BingoNumber:
    def __init__(self, value, checked=False):
        self.value = value
        self.checked = checked
