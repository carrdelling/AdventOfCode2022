
def solve(data):

    score = 0
    for a, b, c in zip(data[::3], data[1::3], data[2::3]):
        common = next(iter(set(a) & set(b) & set(c)))
        score += ord(common) - 38 if ord(common) < 91 else ord(common) - 96

    return score


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            input_.append(row.strip())

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
