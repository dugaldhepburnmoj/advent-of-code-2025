with open("data/day_9.txt") as file:
    locations = [
        [int(coord) for coord in element.split(",")]
        for element in file.read().splitlines()
    ]

print(locations)

n_locations = len(locations)


def area_rect(coord_1, coord_2):
    return (abs(coord_2[0] - coord_1[0]) + 1) * (abs(coord_2[1] - coord_1[1]) + 1)


largest_area = 0

for ii, coord_1 in enumerate(locations):
    for jj in range(ii + 1, n_locations):
        coord_2 = locations[jj]
        new_area = area_rect(coord_1, coord_2)
        if new_area > largest_area:
            largest_area = new_area

print(largest_area)

# %%
# Part 2
