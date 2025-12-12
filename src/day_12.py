import re

with open("data/day_12.txt") as file:
    data = file.read()

parts = data.split("\n\n")

print(parts[0])

possible_count = 0
impossible_count = 0
indeterminate_count = 0

for part in parts:
    shape_match = re.match(r"[0-9]+:\n[#\.\n]+", part, re.DOTALL)

    if shape_match:
        pass
    else:
        for line in part.splitlines():
            region_match = re.match(r"([0-9]+x[0-9]+): ([0-9 ]+)", line, re.DOTALL)

            region_area = [int(element) for element in region_match.group(1).split("x")]
            region_shapes = [
                int(element) for element in region_match.group(2).split(" ")
            ]

            total_region_area = region_area[0] * region_area[1]
            total_shapes_area = (
                region_shapes[0] * 7
                + region_shapes[1] * 7
                + region_shapes[2] * 7
                + region_shapes[3] * 6
                + region_shapes[4] * 6
                + region_shapes[5] * 7
            )
            max_shapes_area = 9 * sum(region_shapes)

            if total_shapes_area > total_region_area:
                # print("Not possible to fit in")
                impossible_count += 1
            elif total_region_area >= max_shapes_area:
                # print("Trivially possible to fit in")
                possible_count += 1
            else:
                print("Indeterminate")
                print(f"{region_area = }")
                print(f"{region_shapes = }")
                print(f"{total_shapes_area = }")
                print(f"{total_region_area = }")
                print(f"{max_shapes_area = }")
                indeterminate_count += 1
                print("=" * 60)

print(f"{impossible_count = }")
print(f"{possible_count = }")
print(f"{indeterminate_count = }")
