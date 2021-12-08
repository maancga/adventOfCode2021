import sys
import utils
from board import Board

INPUT_FILE_NAME = sys.argv[1]
ROWS_SIZE = 5


def main():
    data = utils.get_clean_measurements_from_file(
        INPUT_FILE_NAME)
    total_rows = 0
    total_cols = 0
    for current_measurement in data:
        [first_measurement,
            second_measurenemnt] = current_measurement.split("->")
        [first_m_x_component,
            first_m_y_component] = first_measurement.split(",")
        [second_m_x_component,
            second_m_y_component] = second_measurenemnt.split(",")
        first_m_x_component = int(first_m_x_component)
        first_m_y_component = int(first_m_y_component)
        second_m_x_component = int(second_m_x_component)
        second_m_y_component = int(second_m_y_component)
        if first_m_x_component > total_rows:
            total_rows = first_m_x_component
        if first_m_y_component > total_cols:
            total_cols = first_m_y_component
        if second_m_x_component > total_rows:
            total_rows = second_m_x_component
        if second_m_y_component > total_cols:
            total_cols = second_m_y_component
    matrix = Board(total_cols + 1, total_rows + 1)
    for current_measurement in data:
        [first_measurement,
         second_measurenemnt] = current_measurement.split("->")
        [first_m_x_component,
            first_m_y_component] = first_measurement.split(",")
        [second_m_x_component,
            second_m_y_component] = second_measurenemnt.split(",")
        first_m_x_component = int(first_m_x_component)
        first_m_y_component = int(first_m_y_component)
        second_m_x_component = int(second_m_x_component)
        second_m_y_component = int(second_m_y_component)
        if first_m_x_component == second_m_x_component:
            if first_m_y_component <= second_m_y_component:
                current_point = first_m_y_component
                while current_point <= second_m_y_component:
                    matrix.mark_position(current_point, first_m_x_component)
                    current_point += 1
            else:
                current_point = second_m_y_component
                while current_point <= first_m_y_component:
                    matrix.mark_position(current_point, first_m_x_component)
                    current_point += 1
        if first_m_y_component == second_m_y_component:
            if first_m_x_component <= second_m_x_component:
                current_point = first_m_x_component
                while current_point <= second_m_x_component:
                    matrix.mark_position(first_m_y_component, current_point)
                    current_point += 1
            else:
                current_point = second_m_x_component
                while current_point <= first_m_x_component:
                    matrix.mark_position(first_m_y_component, current_point)
                    current_point += 1
        if not first_m_y_component == second_m_y_component and not first_m_x_component == second_m_x_component:
            if first_m_x_component < second_m_x_component:
                if first_m_y_component < second_m_y_component:
                    current_point_x = first_m_x_component
                    current_point_y = first_m_y_component
                    while current_point_x <= second_m_x_component:
                        matrix.mark_position(current_point_y, current_point_x)
                        current_point_x += 1
                        current_point_y += 1
                else:
                    current_point_x = first_m_x_component
                    current_point_y = first_m_y_component
                    while current_point_x <= second_m_x_component:
                        matrix.mark_position(current_point_y, current_point_x)
                        current_point_x += 1
                        current_point_y -= 1
            else:
                if first_m_y_component < second_m_y_component:
                    current_point_x = first_m_x_component
                    current_point_y = first_m_y_component
                    while current_point_x >= second_m_x_component:
                        matrix.mark_position(current_point_y, current_point_x)
                        current_point_x -= 1
                        current_point_y += 1
                else:
                    current_point_x = first_m_x_component
                    current_point_y = first_m_y_component
                    while current_point_x >= second_m_x_component:
                        matrix.mark_position(current_point_y, current_point_x)
                        current_point_x -= 1
                        current_point_y -= 1
    matrix.print_board()
    print(matrix.count_overlaps())


main()
