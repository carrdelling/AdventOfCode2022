
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def not_reachable(x, y, c):

    for s, d in c.items():
        if d >= distance((x, y), s):
            return False
    return True


def solve(data):

    size = 4000000

    # cache the distances of every sensor
    cache = {s: distance(s, b) for s, b in data}

    solution = None

    for s, d in cache.items():
        print(s)
        if solution is not None:
            continue

        # outer ring (at d+1)
        for dx in range(d+2):

            if solution is not None:
                continue

            dy = d - dx + 1

            for nx, ny in [(s[0] - dx, s[1] - dy),
                           (s[0] - dx, s[1] + dy),
                           (s[0] + dx, s[1] - dy),
                           (s[0] + dx, s[1] + dy)]:

                if 0 <= nx <= size and 0 <= ny <= size:
                    if not_reachable(nx, ny, cache):
                        solution = (nx * size) + ny

    return solution


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            s, b = row.strip().replace('Sensor at ', '').replace(' closest beacon is at ', '').split(':')
            ss = tuple(int(x.split('=')[1]) for x in s.split(', '))
            bb = tuple(int(x.split('=')[1]) for x in b.split(', '))
            input_.append((ss, bb))

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
