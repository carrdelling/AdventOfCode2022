

def show(_earth):

    earth = {}

    for k, v in _earth.items():
        earth[k] = v

    x_min = min(k[0] for k in earth) - 1
    x_max = max(k[0] for k in earth) + 1
    y_min = min(k[1] for k in earth)
    y_max = max(k[1] for k in earth) + 1

    for y in range(y_min, y_max):
        row = []
        for x in range(x_min, x_max):
            s = earth.get((x, y), '.')
            row.append(s)
        print(''.join(row))


def build_earth(data):

    earth = {}

    for section in data:
        a, b = section[0]
        for s in section[1:]:
            c, d = s

            sx, ex = min(a, c), max(a, c)
            sy, ey = min(b, d), max(b, d)

            for x in range(sx, ex + 1):
                for y in range(sy, ey + 1):
                    earth[(x, y)] = '#'

            a, b = c, d

    earth[(500, 0)] = '+'
    return earth


def flow(earth):

    change = True

    while change:

        change = False
        y_max = max(k[1] for k in earth) + 1

        # next sand
        x, y = 500, 0
        moving = True
        while moving:
            moving = False

            # flow down
            if earth.get((x, y+1), '.') == '.' and y + 1 < y_max:
                x, y = x, y + 1
                moving = True
                continue

            # flow left
            if earth.get((x - 1, y + 1), '.') == '.' and y + 1 < y_max:
                x, y = x - 1, y + 1
                moving = True
                continue

            # flow right
            if earth.get((x + 1, y + 1), '.') == '.' and y + 1 < y_max:
                x, y = x + 1, y + 1
                moving = True
                continue

        if earth.get((x, y), '.') != 'o' and y < y_max - 1:
            earth[(x, y)] = 'o'
            change = True


def solve(data):

    # build earth
    earth = build_earth(data)

    flow(earth)
    show(earth)

    solution = sum(1 for v in earth.values() if v == 'o')

    return solution


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            if len(row) < 1:
                continue
            chunks = [tuple(map(int, x.split(','))) for x in row.split(' -> ')]
            input_.append(chunks)
            
    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()


