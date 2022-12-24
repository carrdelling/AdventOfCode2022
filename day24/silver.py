from collections import defaultdict, deque
from itertools import product


def build_winds(size_x, size_y, floor):

    wind_h = defaultdict(set)
    wind_v = defaultdict(set)

    for x, y in product(range(size_x), range(size_y)):

        # right
        if floor[(x + 1, y + 1)] == '>':
            wind_h[(x, y)].add(0)
            yy = (y+1) % size_y
            t = 1

            while yy != y:
                wind_h[(x, yy)].add(t)
                yy = (yy + 1) % size_y
                t += 1

        # left
        if floor[(x + 1, y + 1)] == '<':
            wind_h[(x, y)].add(0)
            yy = (y-1) % size_y
            t = 1

            while yy != y:

                wind_h[(x, yy)].add(t)
                yy = (yy - 1) % size_y
                t += 1

        # down
        if floor[(x + 1, y + 1)] == 'v':
            wind_v[(x, y)].add(0)
            xx = (x+1) % size_x
            t = 1

            while xx != x:
                wind_v[(xx, y)].add(t)
                xx = (xx + 1) % size_x
                t += 1

        # up
        if floor[(x + 1, y + 1)] == '^':
            wind_v[(x, y)].add(0)
            xx = (x-1) % size_x
            t = 1

            while xx != x:
                wind_v[(xx, y)].add(t)
                xx = (xx - 1) % size_x
                t += 1

    return wind_h, wind_v


def solve(floor):

    x_max = max(p[0] for p in floor)
    end = list({p for p, c in floor.items() if p[0] == x_max and c == '.'})[0]

    size_x = end[0] - 1
    size_y = end[1]

    wind_h, wind_v = build_winds(size_x, size_y, floor)

    # search
    states = deque([((0, 0), 1)])
    best_time = 9999999
    seen = set()

    while states:

        pos, time = states.popleft()
        if time >= best_time:
            continue

        if (pos, time) in seen:
            continue
        seen.add((pos, time))

        next_time = time + 1
        time_h = next_time % size_y
        time_v = next_time % size_x

        # exit!!!
        if pos == (size_x - 1, size_y - 1):
            final_time = next_time
            best_time = min(best_time, final_time)

        # up
        if pos[0] > 0:
            new_pos = (pos[0] - 1, pos[1])
            if (time_v not in wind_v[new_pos]) and (time_h not in wind_h[new_pos]):
                states.append((new_pos, next_time))

        # down
        if pos[0] < (size_x - 1):
            new_pos = (pos[0] + 1, pos[1])
            if (time_v not in wind_v[new_pos]) and (time_h not in wind_h[new_pos]):
                states.append((new_pos, next_time))

        # left
        if pos[1] > 0:
            new_pos = (pos[0], pos[1] - 1)
            if (time_v not in wind_v[new_pos]) and (time_h not in wind_h[new_pos]):
                states.append((new_pos, next_time))

        # right
        if pos[1] < (size_y - 1):
            new_pos = (pos[0], pos[1] + 1)
            if (time_v not in wind_v[new_pos]) and (time_h not in wind_h[new_pos]):
                states.append((new_pos, next_time))

        # do nothing
        if time_v not in wind_v[pos] and time_h not in wind_h[pos]:
            states.append((pos, next_time))

    solution = best_time

    return solution


def main():

    input_ = defaultdict(chr)
    with open('input') as in_f:
        for x, row in enumerate(in_f):
            for y, c in enumerate(row.strip()):
                input_[(x, y)] = c
            
    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()


