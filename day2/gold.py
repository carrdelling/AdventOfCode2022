from collections import Counter


def solve(data):

    matches = Counter(x for x in data)

    order = [('B', 'X'), ('C', 'X'), ('A', 'X'),
             ('A', 'Y'), ('B', 'Y'), ('C', 'Y'),
             ('C', 'Z'), ('A', 'Z'), ('B', 'Z'),
             ]

    score = sum([matches[k] * c for c, k in enumerate(order, 1)])

    return score


def main():
    input_ = []
    with open('input') as in_f:
        for row in in_f:
            input_.append(tuple(row.strip().split()))

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":
    main()
