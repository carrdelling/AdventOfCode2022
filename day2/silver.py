from collections import Counter


def match(x, y):

    _type = ord(y) - 87
    _res = 3 if (ord(y) - ord(x)) == 23 else 0 if (ord(y) - ord(x)) in (22, 25) else 6

    return _type + _res


def solve(data):

    matches = Counter(x for x in data)
    score = sum([match(*r) * c for r, c in matches.items()])

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
