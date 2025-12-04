# %%
# Part 1:

import numpy as np

# Define numerical array from input

paper_array = []
with open("data/day_4.txt") as file:
    for ii, line in enumerate(file):
        paper_array.append(
            [
                int(element)
                for element in list(line.strip().replace("@", "1").replace(".", "0"))
            ]
        )
paper_array = np.array(paper_array)


def is_accessible(paper_array, ii, jj):
    max_ii = paper_array.shape[0]
    max_jj = paper_array.shape[1]
    lower_ii = max(0, ii - 1)
    upper_ii = min(max_ii, ii + 1)
    lower_jj = max(0, jj - 1)
    upper_jj = min(max_jj, jj + 1)
    return bool(
        np.sum(paper_array[lower_ii : upper_ii + 1, lower_jj : upper_jj + 1]) < 5
    )


is_accessible_array = np.array(
    [
        [is_accessible(paper_array, ii, jj) for jj in range(0, paper_array.shape[1])]
        for ii in range(0, paper_array.shape[0])
    ]
)
is_accessible_paper = np.logical_and(paper_array, is_accessible_array)
total_accessible_paper = np.sum(is_accessible_paper)

print(f"Part 1: {total_accessible_paper = }")


# %%
# Part 2:

total_removed_paper = total_accessible_paper

while total_accessible_paper > 0:
    # Remove all accessible paper
    paper_array = np.logical_and(paper_array, np.logical_not(is_accessible_array))
    # Re-compute accessible paper
    is_accessible_array = np.array(
        [
            [
                is_accessible(paper_array, ii, jj)
                for jj in range(0, paper_array.shape[1])
            ]
            for ii in range(0, paper_array.shape[0])
        ]
    )
    is_accessible_paper = np.logical_and(paper_array, is_accessible_array)
    total_accessible_paper = np.sum(is_accessible_paper)
    total_removed_paper += total_accessible_paper

print(total_removed_paper)
