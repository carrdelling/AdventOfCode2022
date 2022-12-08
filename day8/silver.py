from collections import defaultdict


def solve(data):

    visible = set()
    max_x = max(x[0] for x in data)
    max_y = max(x[1] for x in data)

    for (x, y), v in data.items():

        can_see = False

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xx = x
            yy = y

            while not can_see:
                if (xx == 0) or (xx == max_x) or (yy == 0) or (yy == max_y):
                    can_see = True

                xx += dx
                yy += dy

                if data.get((xx, yy), 0) >= v:
                    break
        else:
            if can_see:
                visible.add((x, y))

    solution = len(visible)

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
