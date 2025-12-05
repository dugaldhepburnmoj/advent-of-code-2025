# %% Load in input

input_file = open("data/day_5.txt", "r")
input_contents = input_file.readlines()

range_id_split = input_contents.index("\n")

ranges = input_contents[:range_id_split]
available_ids = [int(id.strip()) for id in input_contents[(range_id_split + 1) :]]

# %%
# Part 1

fresh_ranges = []

for fresh_range in ranges:
    fresh_range = [int(id) for id in fresh_range.strip().split("-")]

    fresh_range_dict = {"lower": fresh_range[0], "upper": fresh_range[1]}

    fresh_ranges.append(fresh_range_dict)

fresh_count = 0

for available_id in available_ids:
    fresh = 0
    ii = 0
    terminated = 0

    while terminated == 0:
        fresh_range = fresh_ranges[ii]
        lower = fresh_range["lower"]
        upper = fresh_range["upper"]

        if available_id >= lower and available_id <= upper:
            fresh = 1

        ii += 1

        terminated = (fresh == 1) or (ii == len(fresh_ranges))

    fresh_count += fresh

print(f"Part 1: {fresh_count = }")

# %%
# Part 2:

deleted_list = [0 for fresh_range in fresh_ranges]

fresh_ranges.sort(key=lambda x: (x["lower"], x["upper"]))

merged_fresh_ranges = []

n_fresh_ids = 0

for ii, fresh_range_subj in enumerate(fresh_ranges):
    if deleted_list[ii] or ii == len(fresh_ranges):
        continue

    lower_subject = fresh_range_subj["lower"]
    upper_subject = fresh_range_subj["upper"]

    for jj, fresh_range_comp in enumerate(fresh_ranges[ii + 1 :]):
        if deleted_list[ii + jj + 1]:
            continue

        lower_comp = fresh_range_comp["lower"]
        upper_comp = fresh_range_comp["upper"]

        if (lower_subject <= lower_comp <= upper_subject) or (
            lower_subject <= upper_comp <= upper_subject
        ):
            lower_subject = min(lower_subject, lower_comp)
            upper_subject = max(upper_subject, upper_comp)
            deleted_list[ii] = deleted_list[ii + jj + 1] = 1

    n_fresh_ids += upper_subject - lower_subject + 1

    merged_fresh_ranges.append({"lower": lower_subject, "upper": upper_subject})

print(f"Part 2: {n_fresh_ids = }")
