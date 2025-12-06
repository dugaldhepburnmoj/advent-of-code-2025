# %%
import re
import numpy as np
import math

# %%

numbers_array = []
operators_array = []
with open("data/day_6.txt") as file:
    for ii, line in enumerate(file):
        if re.match(r"^[0-9\s]*$", line):
            numbers_array.append(
                [int(element) for element in list(line.strip().split())]
            )
        elif re.match(r"^[\s/\\*\\+\\-]*$", line):
            operators_array = list(line.strip().split())
        else:
            ValueError("Line doesn't match either expected pattern")

numbers_array = np.array(numbers_array)

answers = []

for ii, column in enumerate(numbers_array.T):
    operator = operators_array[ii]

    if operator == "*":
        answers.append(math.prod(column))
    elif operator == "+":
        answers.append(sum(column))
    else:
        ValueError("Unknown operator")

sum_answers = int(sum(answers))

print(f"Part 1: {sum_answers = }")

# %%

characters_array = []

with open("data/day_6.txt") as file:
    for ii, line in enumerate(file):
        characters_array.append([character for character in line if character != "\n"])

characters_array = np.array(characters_array)
characters_array_t = characters_array.T

# Add a blank final row so that the final problem is calculated in same way as others
characters_array_t = np.r_[
    characters_array_t, [list(" " * characters_array_t.shape[1])]
]

# %%

number_list = []
answers_sum = 0
first_line = 1

for ii, line in enumerate(characters_array_t):
    # print(ii)
    if first_line == 1:
        operator = line[-1]
        number_list.append(int("".join(line[:-1]).strip()))
        first_line = 0
    elif not all(line == " "):
        number_list.append(int("".join(line).strip()))
        first_line = 0
    else:
        if operator == "*":
            answer = math.prod(number_list)
        elif operator == "+":
            answer = sum(number_list)
        else:
            ValueError("Unknown operator")
        number_list = []
        answers_sum += answer
        first_line = 1

print(f"Part 2: {answers_sum = }")
