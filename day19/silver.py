

def get_quality(blueprint):

    _id, ore_cost, clay_cost, obsidian_cost, geode_cost = blueprint
    best = 0
    TIME = 24
    SEEN = set()

    # resources, bots, time
    # ore, clay, obsidian, geode
    states = [(0, 0, 0, 0, 1, 0, 0, 0, TIME)]

    while states:

        current = states.pop()

        SEEN.add(current)
        now = current[-1]

        if len(SEEN) % 1000000 == 0:
            print(current, current[-1], best)

        # can we build a new robot?
        can_geode = (current[0] >= geode_cost[0]) and (current[2] >= geode_cost[1])
        can_obsidian = (current[0] >= obsidian_cost[0]) and (current[1] >= obsidian_cost[1])
        can_clay = current[0] >= clay_cost
        can_ore = current[0] >= ore_cost

        # production
        top_ore = max([ore_cost, clay_cost, obsidian_cost[0], geode_cost[0]])
        max_ore = (now * top_ore)
        max_clay = (now * obsidian_cost[1])
        max_obsidian = (now * geode_cost[1])

        current = (
            min(current[0] + current[4], max_ore), min(current[1] + current[5], max_clay),
            min(current[2] + current[6], max_obsidian), current[3] + current[7],
            current[4], current[5], current[6], current[7], now - 1
        )

        if current[8] == 0:
            best = max(current[3], best)
            continue

        if can_geode:

            new_state = (current[0] - geode_cost[0], current[1], current[2] - geode_cost[1], current[3],
                         current[4], current[5], current[6], current[7] + 1, current[8])
            if new_state not in SEEN:
                states.append(new_state)

            continue

        if can_obsidian:

            new_state = (current[0] - obsidian_cost[0], current[1] - obsidian_cost[1], current[2], current[3],
                         current[4], current[5], current[6] + 1, current[7], current[8])
            if new_state not in SEEN:
                states.append(new_state)

        if can_ore:

            new_state = (current[0] - ore_cost, current[1], current[2], current[3],
                         current[4] + 1, current[5], current[6], current[7], current[8])
            if new_state not in SEEN:
                states.append(new_state)

        if can_clay:
            new_state = (current[0] - clay_cost, current[1], current[2], current[3],
                         current[4], current[5] + 1, current[6], current[7], current[8])
            if new_state not in SEEN:
                states.append(new_state)

        # do nothing
        if current not in SEEN:
            states.append(current)

    solution = best * _id

    return solution


def solve(data):

    qualities = 0
    for blueprint in data:
        quality = get_quality(blueprint)
        print(quality)
        qualities += quality

    return qualities


def main():

    input_ = []
    with open('input') as in_f:
        for idx, row in enumerate(in_f, 1):
            chunks = row.strip()[20:].split()
            ore_cost = int(chunks[3])
            clay_cost = int(chunks[9])
            obsidian_cost = (int(chunks[15]), int(chunks[18]))
            geode_cost = (int(chunks[24]), int(chunks[27]))

            blueprint = (idx, ore_cost, clay_cost, obsidian_cost, geode_cost)
            input_.append(blueprint)

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()

