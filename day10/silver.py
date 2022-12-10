

def solve(data):

    cycle = 0
    value = 1

    signal = []

    for d in data:

        if d[0] == 'noop':
            signal.append(value)
            cycle += 1

        elif d[0] == 'addx':
            signal.append(value)
            cycle += 1
            signal.append(value)
            cycle += 1
            value += (d[1])
        else:
            assert False, d

    targets = [20, 60, 100, 140, 180, 220]

    solution = [signal[t-1] * t for t in targets]

    return sum(solution)


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = row.strip().split()
            if 'add' in row:
                v[1] = int(v[1])
            input_.append(v)
            
    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()

