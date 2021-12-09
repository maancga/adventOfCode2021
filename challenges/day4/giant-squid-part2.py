from board import BingoNumber, Board
import sys
import utils

INPUT_FILE_NAME = "input.txt"
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

    last_winning_number = None
    for draw in bingo_draws:
        last_winning_number = int(draw)
        for current_board in all_boards:
            if (len(all_boards) == 1):
                break
            current_board.mark_number_if_exists(int(draw))
            current_board.check_if_any_row_is_complete()
            current_board.check_if_any_column_is_complete()
            if (current_board.is_complete()):
                all_boards.remove(current_board)

        if (len(all_boards) == 1):
            break

    winning_board = all_boards[0]
    winning_board.print_board()
    for draw in bingo_draws:
        winning_board.mark_number_if_exists(int(draw))
        row_complete = winning_board.check_if_any_row_is_complete()
        column_complete = winning_board.check_if_any_column_is_complete()
        if (row_complete or column_complete):
            last_winning_number = int(draw)
            break

    winning_board.print_unmarked_values()
    winning_board.print_marked_values()
    print(winning_board.summ_of_none_marked())
    print(winning_board.summ_of_none_marked(), last_winning_number)
    result = winning_board.summ_of_none_marked() * last_winning_number
    print(result)


main()
