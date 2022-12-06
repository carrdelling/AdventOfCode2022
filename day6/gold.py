
def solve(data):

    target = 14
    for idx in range(len(data) - target):

        if len(set(data[idx:idx + target])) == target:
            return idx + target

    return 0


def main():

    with open('input') as in_f:
        input_ = in_f.readline().strip()

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()


