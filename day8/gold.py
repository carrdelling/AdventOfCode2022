from collections import defaultdict


def solve(data):

    solution = 0
    max_x = max(x[0] for x in data)
    max_y = max(x[1] for x in data)

    for (x, y), v in data.items():

        score = 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            xx = x
            yy = y
            orig = v
            can_see = False
            p_score = 1

            while not can_see:

                xx += dx
                yy += dy

                if data.get((xx, yy), 0) >= orig:
                    can_see = True

                if (xx <= 0) or (xx >= max_x) or (yy <= 0) or (yy >= max_y):
                    can_see = True

                if not can_see:
                    p_score += 1

            score *= p_score

        solution = max(solution, score)

    return solution


def main():
    input_ = defaultdict(int)
    with open('input') as in_f:
        for r, row in enumerate(in_f):
            for c, v in enumerate(row.strip()):
                input_[(r, c)] = int(v)

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":
    main()

