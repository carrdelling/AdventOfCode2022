

mapping = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2
}

reverse_mapping = {v: k for k, v in mapping.items()}


def solve(data):

    snafu = 0
    for exp in data:
        parse = [mapping[c] for c in exp]

        number = 0
        e = 0
        for n in parse[::-1]:
            number += (n * (5 ** e))
            e += 1
        snafu += number

    keys = []
    carry = 0
    while snafu > 0:
        key = (snafu + carry) % 5
        snafu = (snafu + carry) // 5

        if key > 2:
            key -= 5
            carry = 1
        else:
            carry = 0
        keys.append(reverse_mapping[key])

    solution = ''.join(keys[::-1])

    return solution


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            input_.append(row.strip())
            
    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
