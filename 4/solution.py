import re
from typing import List

# ASSUMPTION - each row in board has 5 entries
ROW_LENGTH = 5

class Board:
    def __init__(self, rows: List[List[int]]):
        self.rows = rows
        # 0 == value unmarked, 1 == value marked
        self.marked_rows = [[0] * ROW_LENGTH for _ in range(len(self.rows))]

    def process_number(self, number: int):
        for i, row in enumerate(self.rows):
            for j, value in enumerate(row):
                if value == number:
                    self.marked_rows[i][j] = 1

    def is_winner(self) -> bool:
        # check rows (horizontal)
        if any([all(marked_row) for marked_row in self.marked_rows]):
            return True

        # check columns (vertical)
        for i in range(ROW_LENGTH):
            if (all([bool(marked_row[i]) for marked_row in self.marked_rows])):
                return True

        return False

    def sum_of_unmarked_numbers(self) -> int:
        sum = 0

        for i, row in enumerate(self.rows):
            for j, value in enumerate(row):
                if not self.is_marked(i, j):
                    sum += value

        return sum

    def is_marked(self, row_index, column_index) -> bool:
        return self.marked_rows[row_index][column_index] == 1

    # returns formatted string of board w/ marked values indicated by green color (probably won't work across all terminals ¯\_(ツ)_/¯)
    # (totally unnecessary but was bored)
    def __repr__(self) -> str:
        result_str = ''

        for i, row in enumerate(self.rows):
            row_str = ''
            for j, value in enumerate(row):
                padded_value = f'{value:02}'

                row_str += f'\033[32m{padded_value}\033[m' if self.is_marked(i, j) else padded_value
                row_str += ' '
            result_str += row_str.rstrip() + '\n'

        return result_str

# ASSUMPTION on input format - raw_board_string looks like this:
# '76 82  2 92 53\n74 33  8 89  3\n80 27 72 26 91\n30 83  7 16  4\n20 56 48  5 13'
def create_board(raw_board_string) -> Board:
    raw_rows = [r for r in raw_board_string.split('\n') if r.strip() != '']

    # A: nested list comprehension one-liner (hard to read)
    # rows = [[int(n) for n in re.split('\s+', raw_row) if n.strip() != ''] for raw_row in raw_rows]
    rows = []
    for raw_row in raw_rows:
        # B: extra verbose
        # raw_numbers = [n for n in re.split('\s+', raw_row) if n.strip() != '']
        # rows.append([int(n) for n in raw_numbers])

        # C: sort of hybrid
        rows.append([int(n) for n in re.split('\s+', raw_row) if n.strip() != ''])

    return Board(rows)

def collect_called_numbers() -> List[int]:
    with open('input.txt', 'r') as file:
        # ASSUMPTION on input format - numbers in first line only
        first_line = file.readline()
        return [int(n) for n in first_line.split(',')]

def collect_boards() -> List[int]:
    with open('input.txt', 'r') as file:
        # ASSUMPTION on input format - ignore the numbers in first line
        file.readline()
        # ASSUMPTION on input format - ignore empty second line
        file.readline()

        return [create_board(line) for line in file.read().split('\n\n')]

def process_number(called_number: int, boards: List[Board]):
    print(f'number called: {called_number}')

    [board.process_number(called_number) for board in boards]

def find_winning_boards(boards: List[Board]) -> List[Board]:
    return [board for board in boards if board.is_winner()]

def part_one():
    boards = collect_boards()

    for called_number in collect_called_numbers():
        process_number(called_number, boards)
        winning_boards = find_winning_boards(boards)
        if len(winning_boards) > 0:
            # technically could be multiple winning at the same time
            for i, winning_board in enumerate(winning_boards):
                print(f'\n\nWINNER #{i + 1}\n')
                print(winning_board)
                print(f'sum of unmarked numbers: {winning_board.sum_of_unmarked_numbers()}')
                print(f'last called number: {called_number}')
                print(f'puzzle_result: {winning_board.sum_of_unmarked_numbers() * called_number}')
            break

def part_two():
    boards = collect_boards()
    last_winning_board = None

    for called_number in collect_called_numbers():
        process_number(called_number, boards)
        winning_boards = find_winning_boards(boards)
        for winning_board in winning_boards:
            if (len(boards) == 1):
                last_winning_board = boards[0]
            else:
                boards.remove(winning_board)
                print(f'Removed winning board, {len(boards)} boards remain')

        if last_winning_board:
            print('\n\nLOSER (last board complete)\n')
            print(winning_board)
            print(f'sum of unmarked numbers: {winning_board.sum_of_unmarked_numbers()}')
            print(f'last called number: {called_number}')
            print(f'puzzle_result: {winning_board.sum_of_unmarked_numbers() * called_number}')

            break

# part_one()
part_two()
