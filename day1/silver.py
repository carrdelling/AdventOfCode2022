

def solve(data):

    current = 0
    best = 0
    for d in data:

        if len(d) > 0:
            current += int(d)
        else:
            best = max(best, current)
            current = 0
    else:
        best = max(best, current)

    return best


def main():

    with open('input') as in_f:
        input_ = [row.strip() for row in in_f]

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()


