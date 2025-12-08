import numpy as np

n_connections = 1000
n_components = 3

input = open("data/day_8.txt").read()

# %%
# Part 1


def distance_2(vertex_1, vertex_2):
    return sum(np.square(np.subtract(vertex_1, vertex_2)))


box_locations = np.array(
    [
        [int(coordinate) for coordinate in position.split(",")]
        for position in input.splitlines()
    ]
)

distance_list = []
# Keep track of which vertices we're comparing at each stage
# This could be calculated fairly easily but this is easier (likely slower)
id_1_list = []
id_2_list = []

for ii, vertex_1 in enumerate(box_locations):
    for jj in range(ii + 1, box_locations.shape[0]):
        vertex_2 = box_locations[jj]
        distance_element = distance_2(vertex_1, vertex_2)

        distance_list.append(distance_element)
        id_1_list.append(ii)
        id_2_list.append(jj)

# Then just find smallest n distances, to avoid sorting whole list
smallest_distances = np.argpartition(distance_list, n_connections)[:n_connections]

# Create list of the 'component id' of each vertex
# And the size of the component containing each vertex
component_ids = np.array(range(box_locations.shape[0]))
component_sizes = np.array([1 for vertex in box_locations])

for index in smallest_distances:
    # Connect up nearest vertices, updating component info
    index_1 = id_1_list[index]
    index_2 = id_2_list[index]

    component_1_id = component_ids[index_1]
    component_2_id = component_ids[index_2]

    if component_1_id == component_2_id:
        continue
    else:
        component_1_indices = np.where(component_ids == component_1_id)[0]
        component_2_indices = np.where(component_ids == component_2_id)[0]

        all_indices = np.append(component_1_indices, component_2_indices)

        # Update component_ids to give all vertices in the newly joined components the same component id
        component_ids[component_2_indices] = component_1_id
        # Calculate the size of the newly joined component and update component_sizes
        component_sizes[all_indices] = (
            component_sizes[index_1] + component_sizes[index_2]
        )

# Then find unique components and their sizes
all_components = set(zip(component_ids, component_sizes))
sizes = [component[1] for component in all_components]

# Then find size of largest n components
largest_sizes = [
    sizes[index] for index in np.argpartition(sizes, -n_components)[-n_components:]
]

print(f"Part 1: product largest component sizes: {np.prod(largest_sizes)}")

# %%
# Part 2

# Hmm looks like we might need to just sort whole list
distance_indices = np.argsort(distance_list)

ii = 0
component_ids = np.array(range(box_locations.shape[0]))
component_sizes = np.array([1 for _ in box_locations])

# Do same operation as above in order of connection distance
# And just stop once all boxes are in same component
while component_sizes[0] < box_locations.shape[0]:
    index = distance_indices[ii]

    index_1 = id_1_list[index]
    index_2 = id_2_list[index]

    component_1_id = component_ids[index_1]
    component_2_id = component_ids[index_2]

    if component_1_id == component_2_id:
        ii += 1
        continue
    else:
        component_1_indices = np.where(component_ids == component_1_id)[0]
        component_2_indices = np.where(component_ids == component_2_id)[0]
        all_indices = np.append(component_1_indices, component_2_indices)

        component_ids[component_2_indices] = component_1_id
        component_sizes[all_indices] = (
            component_sizes[index_1] + component_sizes[index_2]
        )

    ii += 1

last_index = distance_indices[ii - 1]

index_1 = id_1_list[last_index]
index_2 = id_2_list[last_index]

x_coord_1 = box_locations[index_1][0]
x_coord_2 = box_locations[index_2][0]

print(f"Part 2: product of coords = {x_coord_1 * x_coord_2}")
