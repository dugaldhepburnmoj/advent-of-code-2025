# %%
# Read in input
input_file = open("data/day_2.txt")
input = input_file.read()

# Split input into ranges
ranges_list = input.split(",")

# %%
# Part 1

def extract_number_half(number_str: str, upper: bool) -> int:

    if len(number_str) % 2 == 1:
        if upper:
            return 10**(int((len(number_str) - 1)/2)) - 1
        else:
            return 10**(int((len(number_str) - 1)/2))
    else:
        return int(number_str[:int(len(number_str)/2)])

def extract_invalid_codes(range_str: str) -> list[int]:
    lower_limit, upper_limit = range_str.split("-")

    first_element = extract_number_half(lower_limit, upper = False)
    last_element = extract_number_half(upper_limit, upper = True)

    invalid_codes = []

    if first_element <= last_element:
        for ii in range(first_element,last_element+1):
            invalid_code = int(str(ii)*2)
            if invalid_code >= int(lower_limit) and invalid_code <= int(upper_limit):
                invalid_codes.append(invalid_code)

    return(invalid_codes)

all_invalid_codes = []

for range_str in ranges_list:
    invalid_codes = extract_invalid_codes(range_str)
    all_invalid_codes.extend(invalid_codes)

print(f"Part 1: {sum(all_invalid_codes)=}")

# %%
# Part 2

import math

def extract_number_nth(number_str: str, N: int, upper: bool) -> int:

    if upper:
        return int(number_str[:math.ceil(len(number_str)/N)])
    else:
        if len(number_str) < N:
            return 0
        else:
            return int(number_str[:math.floor(len(number_str)/N)])


def extract_invalid_codes_N(upper_limit: str, lower_limit: str, N: int) -> list[int]:

    first_element = extract_number_nth(lower_limit, N, upper = False)
    last_element = extract_number_nth(upper_limit, N, upper = True)

    invalid_codes = []

    if first_element <= last_element:
        for ii in range(first_element,last_element+1):
            invalid_code = int(str(ii)*N)
            if invalid_code >= int(lower_limit) and invalid_code <= int(upper_limit):
                invalid_codes.append(invalid_code)

    return(invalid_codes)

def extract_all_invalid_codes(range_str: str) -> list[int]:
    lower_limit, upper_limit = range_str.split("-")

    all_invalid_codes = set()

    for N in range(2, len(upper_limit)+1):
        invalid_codes = extract_invalid_codes_N(upper_limit, lower_limit, N)
        all_invalid_codes.update(invalid_codes)

    return(all_invalid_codes)

all_invalid_codes = []

for range_str in ranges_list:
    invalid_codes = extract_all_invalid_codes(range_str)
    all_invalid_codes.extend(invalid_codes)

print(f"Part 2: {sum(all_invalid_codes)=}")