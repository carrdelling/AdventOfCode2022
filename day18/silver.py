

def neighbours(x, y, z):

    for _x, _y, _z in [(1, 0, 0), (-1, 0, 0),
                       (0, 1, 0), (0, -1, 0),
                       (0, 0, 1), (0, 0, -1)]:

        yield x + _x, y + _y, z + _z


def solve(data):

    solid = {x for x in data}

    solution = sum(1 for p in data for n in neighbours(*p) if n not in solid)

    return solution


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = tuple(map(int, row.strip().split(',')))
            input_.append(v)
            
    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
