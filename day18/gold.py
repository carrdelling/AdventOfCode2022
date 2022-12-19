
def neighbours(x, y, z):

    for _x, _y, _z in [(1, 0, 0), (-1, 0, 0),
                       (0, 1, 0), (0, -1, 0),
                       (0, 0, 1), (0, 0, -1)]:

        yield x + _x, y + _y, z + _z


def solve(data):

    solid = {x for x in data}
    xs = {x[0] for x in data}
    min_x, max_x = min(xs), max(xs)
    ys = {x[1] for x in data}
    min_y, max_y = min(ys), max(ys)
    zs = {x[2] for x in data}
    min_z, max_z = min(zs), max(zs)

    sx, sy, sz = min_x - 1, min_y - 1, min_z - 1
    ex, ey, ez = max_x + 1, max_y + 1, max_z + 1

    flow = set()
    to_explore = [(sx, sy, sz)]

    while len(to_explore) > 0:

        drop = to_explore.pop()
        flow.add(drop)

        for n in neighbours(*drop):

            if n in flow:
                continue

            if n in solid:
                continue

            if (sx <= n[0] <= ex) and (sy <= n[1] <= ey) and (sz <= n[2] <= ez):
                to_explore.append(n)

    solution = sum(1 for p in data for n in neighbours(*p) if (n not in solid) and (n in flow))

    return solution


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = tuple(map(int, row.strip().split(',')))
            input_.append(v)

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
