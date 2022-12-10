
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

    line = []
    for i, x in enumerate(signal):

        if x - 1 <= i % 40 <= x + 1:
            line.append('#')
        else:
            line.append(' ')

        if i % 40 == 39:
            print(''.join(line))
            line = []

    return ''


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
