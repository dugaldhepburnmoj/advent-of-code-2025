# %%
# Part 1


def find_max_jamps(line: str) -> int:
    max_digit = max([int(digit) for digit in list(line)[:-1]])

    substring = line[(line.find(str(max_digit)) + 1) :]

    max_second_digit = max([int(digit) for digit in list(substring)])

    max_jamps = max_digit * 10 + max_second_digit

    return max_jamps


assert find_max_jamps("987654321111111") == 98
assert find_max_jamps("811111111111119") == 89
assert find_max_jamps("234234234234278") == 78
assert find_max_jamps("818181911112111") == 92

total_jamps = 0

with open("data/day_3.txt") as file:
    for line in file:
        # Increment dial position
        max_jamps = find_max_jamps(line.strip())
        total_jamps += max_jamps

print(f"Part 1: {total_jamps=}")

# %%
# Part 2


def find_max_kth_digit(substring: str, k: int) -> int:
    if k == 1:
        max_digit = max([int(digit) for digit in list(substring)])
    elif k > 1:
        max_digit = max([int(digit) for digit in list(substring)[: -(k - 1)]])
    else:
        ValueError("k should be at least 1")
    return max_digit


def find_kth_substring(substring: str, max_digit: int) -> str:
    new_substring = substring[(substring.find(str(max_digit)) + 1) :]
    return new_substring


def find_max_jamps_n(line: str, n: int) -> int:
    substring = line
    max_jamps = 0

    for ii in range(n, 0, -1):
        max_digit = find_max_kth_digit(substring, ii)

        substring = find_kth_substring(substring, max_digit)

        max_jamps = max_jamps * 10 + max_digit

    return max_jamps


assert find_max_jamps_n("987654321111111", 12) == 987654321111
assert find_max_jamps_n("811111111111119", 12) == 811111111119
assert find_max_jamps_n("234234234234278", 12) == 434234234278
assert find_max_jamps_n("818181911112111", 12) == 888911112111

total_jamps = 0

with open("data/day_3.txt") as file:
    for line in file:
        # Increment dial position
        max_jamps = find_max_jamps_n(line.strip(), 12)
        total_jamps += max_jamps

print(f"Part 2: {total_jamps=}")
