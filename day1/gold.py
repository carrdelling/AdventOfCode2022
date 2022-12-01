
def solve(data):

    current = 0
    found = []
    for d in data:

        if len(d) > 0:
            current += int(d)
        else:
            found.append(current)
            current = 0
    else:
        found.append(current)
        found.sort(reverse=True)

    return sum(found[:3])


def main():

    with open('input') as in_f:
        input_ = [row.strip() for row in in_f]

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()


