import re
from typing import Dict, List

LINE_REGEX = re.compile('^(\d+),(\d+) -> (\d+),(\d+)$')

simple_testing_lines = [
    # horizontal
    { 'x1': 0, 'y1': 2, 'x2': 4, 'y2': 2 },
    { 'x1': 3, 'y1': 1, 'x2': 5, 'y2': 1 },
    { 'x1': 4, 'y1': 2, 'x2': 1, 'y2': 2 },

    # vertical
    { 'x1': 0, 'y1': 1, 'x2': 0, 'y2': 3 },
    { 'x1': 4, 'y1': 4, 'x2': 4, 'y2': 2 },

    # diagonal
    { 'x1': 0, 'y1': 0, 'x2': 2, 'y2': 2 }, # towards bottom right
    { 'x1': 2, 'y1': 0, 'x2': 4, 'y2': 2 }, # towards bottom right
    { 'x1': 2, 'y1': 3, 'x2': 4, 'y2': 1 }, # towards upper right
    { 'x1': 3, 'y1': 1, 'x2': 2, 'y2': 2 }, # towards bottom left
    { 'x1': 1, 'y1': 3, 'x2': 0, 'y2': 2 }, # towards upper left
]

def collect_lines() -> List[Dict[str, int]]:
    lines = []

    with open('input.txt', 'r') as file:
        for line in file:
            match = LINE_REGEX.match(line)
            x1, y1 = int(match.group(1)), int(match.group(2))
            x2, y2 = int(match.group(3)), int(match.group(4))

            lines.append({ 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2 })

            # only include horizontal & vertical lines
            # if (x1 == x2 or y1 == y2):
                # lines.append({ 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2 })

    return lines

# initialize empty grid w/ 0 at each point
def initialize_grid(lines: List[Dict[str, int]]) -> List[List[int]]:
    max_x, max_y = 0, 0

    for line in lines:
        max_x = max([max_x, line['x1'], line['x2']])
        max_y = max([max_y, line['y1'], line['y2']])

    grid = [[0] * (max_x + 1) for _ in range(max_y + 1)]

    return grid

def mark_grid(grid: List[List[int]], lines: List[Dict[str, int]], include_diagonal: bool = False) -> List[List[int]]:
    for line in lines:
        if line['x1'] == line['x2']: # vertical line
            grid = mark_horizontal_line(grid, line)
        elif line['y1'] == line['y2']: # horizontal line
            grid = mark_vertical_line(grid, line)
        elif include_diagonal: # diagonal line
            grid = mark_diagonal_line(grid, line)

    return grid

def mark_horizontal_line(grid: List[List[int]], line: Dict[str, int]) -> List[List[int]]:
    row_index = line['x1']

    range_start = min(line['y1'], line['y2'])
    range_end = (max(line['y1'], line['y2'])) + 1

    for i in range(range_start, range_end):
        grid[i][row_index] = grid[i][row_index] + 1

    return grid

def mark_vertical_line(grid: List[List[int]], line: Dict[str, int]) -> List[List[int]]:
    column_index = line['y1']

    range_start = min(line['x1'], line['x2'])
    range_end = (max(line['x1'], line['x2'])) + 1

    for i in range(range_start, range_end):
        grid[column_index][i] = grid[column_index][i] + 1

    return grid

# CONSTRAINT: diagonal must be strictly 45 degrees
def mark_diagonal_line(grid: List[List[int]], line: Dict[str, int]) -> List[List[int]]:
    column_start_index = line['x1']
    row_start_index, row_end_index = line['y1'], line['y2']

    line_length = abs(row_end_index - row_start_index) + 1

    # line direction is positive on X axis (e.g. going right)
    x_trend_positive = line['x2'] > line['x1']
    # line direction is positive on Y axis (e.g. going down)
    y_trend_positive = line['y2'] > line['y1']

    pointer = 0

    while (pointer < line_length):
        if x_trend_positive:
            column_index = column_start_index + pointer
        else:
            column_index = column_start_index - pointer

        if y_trend_positive:
            row_index = row_start_index + pointer
        else:
            row_index = row_start_index - pointer

        grid[row_index][column_index] = grid[row_index][column_index] + 1

        pointer += 1

    return grid

def count_overlap_points(grid: List[List[int]]) -> int:
    overlap_count = 0

    for row in grid:
        [overlap_count := overlap_count + 1 for point in row if point >= 2]

    return overlap_count

def part_one():
    # grid = initialize_grid(simple_testing_lines)
    # grid = mark_grid(grid, simple_testing_lines)

    # [print(row) for row in grid]

    lines = collect_lines()
    grid = initialize_grid(lines)
    grid = mark_grid(grid, lines)

    overlap_count = count_overlap_points(grid)

    print(f'number points where 2 or more lines overlap (horizontal + vertical only): {overlap_count}')

def part_two():
    # grid = initialize_grid(simple_testing_lines)
    # grid = mark_grid(grid, simple_testing_lines, True)

    # [print(row) for row in grid]

    lines = collect_lines()
    grid = initialize_grid(lines)
    grid = mark_grid(grid, lines, True)
    overlap_count = count_overlap_points(grid)

    print(f'number points where 2 or more lines overlap (horizontal, vertical, diagonal): {overlap_count}')

part_one()
part_two()
