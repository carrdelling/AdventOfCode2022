

def chase(h, t):

    delta = h[0] - t[0], h[1] - t[1]
    r = t[0], t[1]

    if delta[0] == 0:
        if delta[1] > 1:
            r = t[0], t[1] + 1
        elif delta[1] < -1:
            r = t[0], t[1] - 1
        else:
            pass
    elif delta[1] == 0:
        if delta[0] > 1:
            r = t[0] + 1, t[1]
        elif delta[0] < -1:
            r = t[0] - 1, t[1]
        else:
            pass
    else:
        if delta[0] == 2:
            if delta[1] > 0:
                r = t[0] + 1, t[1] + 1
            elif delta[1] < 0:
                r = t[0] + 1, t[1] - 1
            else:
                pass
        elif delta[0] == -2:
            if delta[1] > 0:
                r = t[0] - 1, t[1] + 1
            elif delta[1] < 0:
                r = t[0] - 1, t[1] - 1
            else:
                pass
        elif delta[1] == 2:
            if delta[0] > 0:
                r = t[0] + 1, t[1] + 1
            elif delta[0] < 0:
                r = t[0] - 1, t[1] + 1
            else:
                pass
        elif delta[1] == -2:
            if delta[0] > 0:
                r = t[0] + 1, t[1] - 1
            elif delta[0] < 0:
                r = t[0] - 1, t[1] - 1
            else:
                pass
        elif abs(delta[0]) == 1 and abs(delta[1]) == 1:
            pass
        else:
            assert False, (delta, h, t)

    return r


def solve(data):

    visited = set()
    rope = [(0, 0) for _ in range(10)]

    for d, v in data:
        vv = v

        while vv > 0:
            if d == 'U':
                rope[0] = rope[0][0] - 1, rope[0][1]
            if d == 'D':
                rope[0] = rope[0][0] + 1, rope[0][1]
            if d == 'L':
                rope[0] = rope[0][0], rope[0][1] - 1
            if d == 'R':
                rope[0] = rope[0][0], rope[0][1] + 1

            vv -= 1

            for idx in range(9):
                rope[idx+1] = chase(rope[idx], rope[idx+1])

            visited.add(rope[9])

    return len(visited)


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            d, v = row.strip().split()
            input_.append((d, int(v)))

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
