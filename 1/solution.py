def collect_measurements():
    with open('input.txt', 'r') as file:
        measurements = [int(line.strip()) for line in file]

    return measurements

def part_one():
    measurements = collect_measurements()
    number_increases = 0
    previous_measurement = measurements[0]

    for measurement in measurements[1:]:
        if measurement > previous_measurement:
            number_increases += 1

        previous_measurement = measurement

    print(f'Number of increases from previous measurement: {number_increases}')

def part_two():
    window_size = 3

    measurements = collect_measurements()
    number_increases = 0

    for (index, _) in enumerate(measurements):
        current_window = measurements[index:(index + window_size)]
        current_window_sum = sum(current_window)


        if index == 0:
            previous_window_sum = current_window_sum
            continue

        if current_window_sum > previous_window_sum:
            number_increases += 1

        previous_window_sum = current_window_sum

    print(f'Number of increases from previous window: {number_increases}')

# part_one()
part_two()
