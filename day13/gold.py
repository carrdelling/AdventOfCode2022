from functools import cmp_to_key


def check_order(a, b):

    if isinstance(a, int) and isinstance(b, int):
        return a - b

    if isinstance(a, int) and isinstance(b, list):
        return check_order([a], b)

    if isinstance(a, list) and isinstance(b, int):
        return check_order(a, [b])

    if isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            part = check_order(x, y)
            if part == 0:
                # go to the next
                continue
            else:
                return part

        # if all matching elements are equal, return left difference
        return len(a) - len(b)


def solve(data):

    # dividers
    full = [[[2]], [[6]]]

    for a, b in data:
        full.append(a)
        full.append(b)

    full.sort(key=cmp_to_key(check_order))

    solution = 1
    for i, f in enumerate(full, 1):
        if f == [[2]] or f == [[6]]:
            solution *= i

    return solution


def main():

    input_ = []
    with open('input') as in_f:
        pair = []
        for row in in_f:
            if len(row) < 2:
                continue
            if not pair:
                pair.append(eval(row.strip()))
            else:
                pair.append(eval(row.strip()))
                input_.append(tuple(pair))
                pair = []

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
