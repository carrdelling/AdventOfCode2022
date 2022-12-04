
def overlap(a, b, c, d):

    if a <= c and b >= d:
        return 1
    if c <= a and d >= b:
        return 1

    return 0


def solve(data):

    solution = sum(overlap(a, b, c, d) for (a, b), (c, d) in data)

    return solution


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            pairs = [tuple(map(int, p.split('-'))) for p in row.strip().split(',')]

            input_.append(pairs)
            
    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()


