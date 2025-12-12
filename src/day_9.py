with open("data/day_9.txt") as file:
    locations = [
        [int(coord) for coord in element.split(",")]
        for element in file.read().splitlines()
    ]

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

print(f"Part 1: {largest_area= }")

# %%
# Part 2

x_compression = {
    coord: ii
    for ii, coord in enumerate(sorted(set([location[0] for location in locations])))
}
y_compression = {
    coord: ii
    for ii, coord in enumerate(sorted(set([location[1] for location in locations])))
}

x_compressed = [x_compression[location[0]] for location in locations]
y_compressed = [y_compression[location[1]] for location in locations]

red_locations_compressed = {
    (x_coord, y_compressed[ii]) for ii, x_coord in enumerate(x_compressed)
}

green_locations_compressed = set()

for ii in range(n_locations):
    for jj in range(ii + 1, n_locations):
        x_compressed_1 = x_compressed[ii]
        y_compressed_1 = y_compressed[ii]
        x_compressed_2 = x_compressed[jj]
        y_compressed_2 = y_compressed[jj]

        if x_compressed_1 == x_compressed_2:
            if y_compressed_1 > y_compressed_2:
                y_min = y_compressed_2
                y_max = y_compressed_1
            else:
                y_min = y_compressed_1
                y_max = y_compressed_2
            to_add = [
                (x_compressed_1, y_coord_compressed)
                for y_coord_compressed in range(y_min + 1, y_max)
            ]
            green_locations_compressed.update(to_add)
        elif y_compressed_1 == y_compressed_2:
            if x_compressed_1 > x_compressed_2:
                x_min = x_compressed_2
                x_max = x_compressed_1
            else:
                x_min = x_compressed_1
                x_max = x_compressed_2
            to_add = [
                (x_coord_compressed, y_compressed_1)
                for x_coord_compressed in range(x_min + 1, x_max)
            ]
            green_locations_compressed.update(to_add)

to_process = {(-1, -1)}
max_x_compressed = len(x_compression)
max_y_compressed = len(y_compression)


def add_coords(coord_1, coord_2):
    return (coord_1[0] + coord_2[0], coord_1[1] + coord_2[1])


directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}

outside_locations = set()

while to_process:
    processing = to_process.pop()
    if (
        processing in green_locations_compressed
        or processing in red_locations_compressed
        or processing in outside_locations
        or not (-1 <= processing[0] <= max_x_compressed + 1)
        or not (-1 <= processing[1] <= max_y_compressed + 1)
    ):
        continue
    else:
        outside_locations.add(processing)
        to_process.update(add_coords(processing, direction) for direction in directions)


largest_area = 0

for ii in range(n_locations):
    for jj in range(ii + 1, n_locations):
        coord_1 = locations[ii]
        coord_2 = locations[jj]
        new_area = area_rect(coord_1, coord_2)

        if new_area > largest_area:
            x_compressed_1 = x_compressed[ii]
            y_compressed_1 = y_compressed[ii]
            x_compressed_2 = x_compressed[jj]
            y_compressed_2 = y_compressed[jj]

            if x_compressed_1 >= x_compressed_2:
                x_min = x_compressed_2
                x_max = x_compressed_1

            else:
                x_min = x_compressed_1
                x_max = x_compressed_2

            if y_compressed_1 >= y_compressed_2:
                y_min = y_compressed_2
                y_max = y_compressed_1
            else:
                y_min = y_compressed_1
                y_max = y_compressed_2

            top_edge = {
                (x_coord_compressed, y_max)
                for x_coord_compressed in range(x_min, x_max + 1)
            }
            bottom_edge = {
                (x_coord_compressed, y_min)
                for x_coord_compressed in range(x_min, x_max + 1)
            }
            right_edge = {
                (x_max, y_coord_compressed)
                for y_coord_compressed in range(y_min, y_max + 1)
            }
            left_edge = {
                (x_min, y_coord_compressed)
                for y_coord_compressed in range(y_min, y_max + 1)
            }

            edge_set = top_edge.union(bottom_edge, right_edge, left_edge)
            outside_edge_set = edge_set.intersection(outside_locations)

            if outside_edge_set:
                continue
            else:
                largest_area = new_area

print(f"Part 2: {largest_area = }")
