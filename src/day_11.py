import functools

connections = {}

with open("data/day_11.txt") as file:
    for ii, line in enumerate(file):
        line_split = line.split(":")
        key = line_split[0].strip()
        out_conns = [out_conn.strip() for out_conn in line_split[1].split()]

        connections[key] = out_conns


@functools.cache
def calculate_routes(start_node, end_node):
    if start_node == end_node:
        return 1
    elif start_node not in connections:
        return 0
    else:
        return sum(
            [
                calculate_routes(next_node, end_node)
                for next_node in connections[start_node]
            ]
        )


you_routes = calculate_routes("you", "out")

print(f"{you_routes = }")

dac_fft_routes = calculate_routes("dac", "fft")
fft_dac_routes = calculate_routes("fft", "dac")

print(f"{dac_fft_routes = }")
print(f"{fft_dac_routes = }")

if dac_fft_routes > 0 and fft_dac_routes == 0:
    svr_routes = (
        calculate_routes("svr", "dac") * dac_fft_routes * calculate_routes("fft", "out")
    )
elif fft_dac_routes > 0 and dac_fft_routes == 0:
    svr_routes = (
        calculate_routes("svr", "fft") * fft_dac_routes * calculate_routes("dac", "out")
    )
else:
    ValueError(
        "Input contains loops (or assumptions are otherwise wrong) - revisit approach"
    )

print(f"{svr_routes = }")
