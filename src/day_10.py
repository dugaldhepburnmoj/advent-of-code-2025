import re
import numpy as np
from itertools import combinations
import scipy.optimize

total_buttons_pressed = 0

with open("data/day_10.txt") as file:
    for ii, line in enumerate(file):
        line_match = re.match(r"\[([\#\.]+)\] ([0-9\,\(\) ]+) (\{[0-9\,]+\})", line)
        lights = [
            int(light)
            for light in line_match.group(1).replace("#", "1").replace(".", "0")
        ]
        buttons = [
            [int(element) for element in button[1:-1].split(",")]
            for button in line_match.group(2).split()
        ]

        n_lights = len(lights)
        n_buttons = len(buttons)

        finished = False

        if all([light == 0 for light in lights]):
            finished = True
            break
        else:
            count_buttons_pressed = 1

            while not finished:
                selections = combinations(list(buttons), count_buttons_pressed)
                for buttons_pressed in selections:
                    light_attempt = np.array(lights)

                    for button in buttons_pressed:
                        light_attempt[button] += 1

                    if all([light % 2 == 0 for light in light_attempt]):
                        total_buttons_pressed += len(buttons_pressed)
                        finished = True
                        break

                count_buttons_pressed += 1

print(f"Part 1: total button presses = {total_buttons_pressed}")

# Part 2
# Had to rely on scipy.optimize for this part, as trying pathfinding/search approach as above quickly becomes intractable
# And it is just an integer programming problem
total_buttons_pressed_2 = 0

with open("data/day_10.txt") as file:
    for ii, line in enumerate(file):
        line_match = re.match(r"\[([\#\.]+)\] ([0-9\,\(\) ]+) \{([0-9\,]+)\}", line)

        joltages = [int(element) for element in line_match.group(3).split(",")]

        buttons = [
            [int(element) for element in button[1:-1].split(",")]
            for button in line_match.group(2).split()
        ]

        n_lights = len(joltages)
        n_buttons = len(buttons)

        A_eq = [
            [1 if ii in button else 0 for button in buttons] for ii in range(n_lights)
        ]

        result = scipy.optimize.linprog(
            c=[1] * n_buttons, A_eq=A_eq, b_eq=joltages, integrality=True
        )

        total_buttons_pressed_2 += int(result.fun)

print(f"Part 2: total button presses = {total_buttons_pressed_2}")
