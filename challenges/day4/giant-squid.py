from board import BingoNumber, Board
import sys
import utils

INPUT_FILE_NAME = sys.argv[1]
ROWS_SIZE = 5


def main():
    data = utils.get_clean_measurements_from_file(
        INPUT_FILE_NAME)
    data_with_no_empty_lines = list(filter(lambda line: line != "", data))
    current_line_index = 0
    bingo_draws = data_with_no_empty_lines[current_line_index]
    bingo_draws = list(map(int, bingo_draws.split(",")))
    current_line_index += 1
    all_boards = []
    while current_line_index < len(data_with_no_empty_lines):
        current_board = Board(ROWS_SIZE, ROWS_SIZE)
        for row in range(ROWS_SIZE):
            current_row = data_with_no_empty_lines[current_line_index]
            current_row_list = current_row.split()
            current_row_list_as_ints = map(int, current_row_list)
            for index, element in enumerate(current_row_list_as_ints):
                current_board.content[row][index] = BingoNumber(element)
            current_line_index += 1
        all_boards.insert(len(all_boards), current_board)

    winning_board = None
    last_winning_number = None
    for draw in bingo_draws:
        for current_board in all_boards:
            current_board.mark_number_if_exists(int(draw))
            row_complete = current_board.check_if_any_row_is_complete()
            column_complete = current_board.check_if_any_column_is_complete()
            if (row_complete or column_complete):
                last_winning_number = int(draw)
                winning_board = current_board
                break
        if (row_complete or column_complete):
            break
    result = winning_board.summ_of_none_marked() * last_winning_number
    print(result)


main()
