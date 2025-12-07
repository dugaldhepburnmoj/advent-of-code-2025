import re
import numpy as np

# %% 
# Part 1

input = open("data/day_7.txt").read()

tachyon_locations = {input.splitlines()[0].find("S")}

total_splits = 0

for ii, line in enumerate(input.splitlines()):

    splitter_locations = {splitter_match.start(0) for splitter_match in re.finditer(r"\^", line)}
    new_tachyon_locations = set()

    if splitter_locations:
        for tachyon_location in tachyon_locations:
            if tachyon_location in splitter_locations:
                new_tachyon_locations.update([tachyon_location-1, tachyon_location+1])
                total_splits += 1
            else:
                new_tachyon_locations.add(tachyon_location)
    else:
        new_tachyon_locations = tachyon_locations

    tachyon_locations = new_tachyon_locations

print(f"Part 1: {total_splits = }")

# %%
# Part 2

line = input.splitlines()[0]

tachyon_locations = {line.find("S")}

total_routes = np.array([0 for _ in line])
total_routes[list(tachyon_locations)] = 1

for ii, line in enumerate(input.splitlines()):

    splitter_locations = {splitter_match.start(0) for splitter_match in re.finditer(r"\^", line)}
    new_tachyon_locations = set()

    if splitter_locations:
        for tachyon_location in tachyon_locations:
            if tachyon_location in splitter_locations:
                new_tachyon_locations.update([tachyon_location-1, tachyon_location+1])
                total_routes[tachyon_location-1] = total_routes[tachyon_location-1] + total_routes[tachyon_location]
                total_routes[tachyon_location+1] = total_routes[tachyon_location+1] + total_routes[tachyon_location]
                total_routes[tachyon_location] = 0
            else:
                new_tachyon_locations.add(tachyon_location)
    else:
        new_tachyon_locations = tachyon_locations

    tachyon_locations = new_tachyon_locations

print(f"Part 2: total_routes = {sum(total_routes)}")

    