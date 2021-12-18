def process_command(line):
    direction, distance = line.split(' ')
    distance = int(distance)

    return dict(direction=direction, distance=distance)

def collect_commands():
    with open('input.txt', 'r') as file:
        commands = list(map(process_command, file))

    return commands

def part_one():
    horizontal_position, depth = 0, 0

    commands = collect_commands()
    for command in commands:
        direction, distance = command['direction'], command['distance']

        if direction == 'down':
            depth += distance
        elif direction == 'up':
            depth -= distance
        elif direction == 'forward':
            horizontal_position += distance

    print(f'final horizontal_position: {horizontal_position}, depth: {depth}, multiplied: {horizontal_position * depth}')

def part_two():
    horizontal_position, depth, aim  = 0, 0, 0

    commands = collect_commands()
    for command in commands:
        direction, distance = command['direction'], command['distance']

        if direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance
        elif direction == 'forward':
            horizontal_position += distance
            depth += (aim * distance)

    print(f'final horizontal_position: {horizontal_position}, depth: {depth}, aim: {aim}, (horizontal_position * depth): {horizontal_position * depth}')

# part_one()
part_two()