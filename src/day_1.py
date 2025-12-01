# %%

# Part 1:

# Initialise dial, number of zeros
dial_position = 50
n_zeros = 0

with open("data/day_1.txt") as file:
    for line in file:
        # Increment dial position
        change = int(line.replace("L", "-").replace("R", "").strip())
        dial_position += change

        # Check if dial is pointing at zero:
        if dial_position % 100 == 0:
            n_zeros += 1

print(f"Part 1: {n_zeros=}")  # %%

# Part 2
import math

# Initialise dial, number of zeros
dial_position = 50
n_zeros = 0

with open("data/day_1.txt") as file:
    for line in file:
        # Increment dial position
        change = int(line.replace("L", "-").replace("R", "").strip())
        old_dial_position = dial_position
        dial_position += change

        # Now just care about total passes of zero
        n_zero_increment = abs(
            math.floor(dial_position / 100) - math.floor(old_dial_position / 100)
        )

        # This doesn't account for starting/ending on multiple of 100 correctly
        # e.g. 157 -> 100 should increment count by 1, but formula gives 0

        if change < 0 and dial_position % 100 == 0:
            n_zero_increment += 1

        if change < 0 and old_dial_position % 100 == 0:
            n_zero_increment -= 1

        n_zeros += n_zero_increment

print(f"Part 2: {n_zeros=}")

# %%
