from collections import defaultdict


def rotate_order(o):

    return o[1:] + o[:1]


def get_targets(p, dir_):

    deltas = {'N': {(-1, -1), (-1, 0), (-1, 1)},
              'S': {(1, -1), (1, 0), (1, 1)},
              'W': {(-1, -1), (0, -1), (1, -1)},
              'E': {(-1, 1), (0, 1), (1, 1)}
               }

    targets = {(p[0] + dx, p[1] + dy) for dx, dy in deltas[dir_]}

    return targets


def check_none(p, data):

    for dx, dy in {(-1, -1), (-1, 0), (-1, 1),
                   (0, -1),  (0, 1),
                   (1, -1), (1, 0), (1, 1)}:
        if (p[0] + dx, p[1] + dy) in data:
            return False
    return True


def move(p, dir_):

    deltas = {'N': (-1, 0),
              'S': (1, 0),
              'W': (0, -1),
              'E': (0, 1)
               }

    return p[0] + deltas[dir_][0], p[1] + deltas[dir_][1]


def show(data):

    min_x = min(x[0] for x in data)
    min_y = min(x[1] for x in data)
    max_x = max(x[0] for x in data)
    max_y = max(x[1] for x in data)

    screen = []

    for x in range(min_x, max_x + 1):
        row = []
        for y in range(min_y, max_y + 1):
            if (x, y) in data:
                row.append('#')
            else:
                row.append('.')
        screen.append(''.join(row))

    print('\n'.join(screen))


def solve(data):

    ORDER = ['N', 'S', 'W', 'E']
    ROUNDS = 10000

    solution = 0

    for round in range(ROUNDS):

        # announce proposal
        changes = defaultdict(list)
        is_moving = False
        for p in data:

            if check_none(p, data):
                continue
            for o in ORDER:
                targets = get_targets(p, o)
                if len(data & targets) == 0:
                    new = move(p, o)
                    changes[new].append(p)
                    break

        # move!
        for pos, q in changes.items():
            if len(q) != 1:
                continue
            old = q[0]

            data.discard(old)
            data.add(pos)
            is_moving = True

        ORDER = rotate_order(ORDER)

        if not is_moving:
            solution = round + 1
            break

    return solution


def main():

    input_ = set()
    with open('input') as in_f:
        for x, row in enumerate(in_f):
            for y, c in enumerate(row.strip()):
                if c == '#':
                    input_.add((x, y))

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
