from collections import defaultdict


def neighbours(x, y):

    for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        yield x + _x, y + _y


def solve(data):

    current = list({(k[0], k[1]) for k, x in data.items() if x == 83})[0]
    steps = 0
    visited = {}
    states = [(current, steps)]
    best = 9999999

    while states:

        p, s = states.pop()

        if visited.get(p, 999999) <= s:
            continue

        if data[p] == 69:
            best = min(best, s)

        visited[p] = min(visited.get(p, 999999), s)

        for n in neighbours(p[0], p[1]):

            if visited.get(n, 999999) <= s:
                continue

            ch = max(data[p], 97)
            nh = data[n]
            nh = ord('z') if nh == 69 else nh

            if nh <= ch + 1:
                states.append((n, s + 1))

    return best


def main():

    input_ = defaultdict(lambda: 999)
    with open('input') as in_f:
        for x, row in enumerate(in_f):
            for y, c in enumerate(row.strip()):
                v = ord(c)
                input_[(x, y)] = v

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
