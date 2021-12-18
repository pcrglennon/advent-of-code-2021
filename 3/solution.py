from typing import Dict, List

# ASSUMPTION - all binary numbers in input are 12 digits
DIGITS_LENGTH = 12

def collect_numbers() -> List[str]:
    with open('input.txt', 'r') as file:
        numbers = [line.rstrip('\n') for line in file]

    return numbers

# returns dict w/ most common bit value (as string) by index, e.g. { 0: '1', 1: '1', 2: '0' }
# NB - if both 0 and 1 are equally common, chooses 1 as the winner
def most_common_bits_by_index(numbers) -> Dict[int, str]:
    numbers_count = len(numbers)

    # track number of "1" bits at each index over all the numbers
    one_bit_counts = [0 for _ in range(DIGITS_LENGTH)]
    most_common_bits = {}

    for number in numbers:
        for index in range(DIGITS_LENGTH):
            if number[index] == '1':
                one_bit_counts[index] += 1

    for index in range(DIGITS_LENGTH):
        if one_bit_counts[index] >= (numbers_count / 2):
            most_common_bits[index] = '1'
        else:
            most_common_bits[index] = '0'

    return most_common_bits

def part_one():
    numbers = collect_numbers()
    most_common_bits = most_common_bits_by_index(numbers)

    gamma_rate_binary_str, epsilon_rate_binary_str = '', ''

    for index in range(DIGITS_LENGTH):
        if most_common_bits[index] == 1:
            gamma_rate_binary_str += '1'
            epsilon_rate_binary_str += '0'
        else:
            gamma_rate_binary_str += '0'
            epsilon_rate_binary_str += '1'

    gamma_rate_int = int(gamma_rate_binary_str, 2)
    epsilon_rate_int = int(epsilon_rate_binary_str, 2)

    print(f'gamma_rate_binary_str: {gamma_rate_binary_str}, gamma_rate_int: {gamma_rate_int}')
    print(f'epsilon_rate_binary_str: {epsilon_rate_binary_str}, epsilon_rate_int: {epsilon_rate_int}')
    print(f'power consumption (gamma_rate_int * epsilon_rate_int): {gamma_rate_int * epsilon_rate_int}')

def part_two():
    # Misunderstood the problem at first - at first I thought "the most common bit" was static based on # original input set, didn't realize I had to re-calculate after each round of filtering!
    #
    # numbers = collect_numbers()
    # most_common_bits = most_common_bits_by_index(numbers)
    # oxygen_rating_candidates, co2_rating_candidates = numbers, numbers
    # ratings_index = 0
    #
    # while (
    #     ratings_index < DIGITS_LENGTH and
    #     (len(oxygen_rating_candidates) > 1 or len(co2_rating_candidates) > 1)
    # ):
    #     most_common_bit = most_common_bits[ratings_index]

    #     oxygen_rating_candidates = [c for c in oxygen_rating_candidates if c[ratings_index] == most_common_bit]
    #     co2_rating_candidates = [c for c in co2_rating_candidates if c[ratings_index] != most_common_bit]

    #     ratings_index += 1

    oxygen_rating_candidates, co2_rating_candidates = collect_numbers(), collect_numbers()
    oxygen_rating_index, co2_rating_index = 0, 0

    while oxygen_rating_index < DIGITS_LENGTH and len(oxygen_rating_candidates) > 1:
        most_common_bits = most_common_bits_by_index(oxygen_rating_candidates)
        most_common_bit = most_common_bits[oxygen_rating_index]

        oxygen_rating_candidates = [c for c in oxygen_rating_candidates if c[oxygen_rating_index] == most_common_bit]

        oxygen_rating_index += 1

    while co2_rating_index < DIGITS_LENGTH and len(co2_rating_candidates) > 1:
        most_common_bits = most_common_bits_by_index(co2_rating_candidates)
        most_common_bit = most_common_bits[co2_rating_index]

        co2_rating_candidates = [c for c in co2_rating_candidates if c[co2_rating_index] != most_common_bit]

        co2_rating_index += 1

    oxygen_rating_number = oxygen_rating_candidates[0]
    oxygen_rating_int = int(oxygen_rating_number, 2)

    co2_rating_number = co2_rating_candidates[0]
    co2_rating_int = int(co2_rating_number, 2)

    life_support_rating = oxygen_rating_int * co2_rating_int

    print('\n\n')
    print(f'oxygen_rating_number: {oxygen_rating_number}, int: {oxygen_rating_int}')
    print(f'co2_rating_number: {co2_rating_number}, int: {co2_rating_int}')
    print(f'life_support_rating: {life_support_rating}')

# part_one()
part_two()