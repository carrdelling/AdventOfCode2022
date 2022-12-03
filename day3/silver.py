
def solve(data):

    sol = 0
    for sack in data:
        n = len(sack) // 2
        left, right = set(sack[:n]), set(sack[n:])
        c = next(iter(left & right))

        score = ord(c) - 38 if ord(c) < 91 else ord(c) - 96
        sol += score

    return sol


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            input_.append(row.strip())
            
    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
