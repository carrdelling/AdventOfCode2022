

def find(tag, arr, f_value=False):

    idx = 0
    part = 1 if f_value else 0
    while True:
        if arr[idx][part] == tag:
            return idx
        idx += 1


def solve(data):

    arr = [(idx, v * 811589153) for idx, v in enumerate(data)]
    N = len(data)

    for _ in range(10):
        for i in range(N):

            pos = find(i, arr)

            val = arr[pos][1]
            new_pos = (pos + val) % (N - 1)

            arr = arr[:pos] + arr[pos+1:]
            arr = arr[:new_pos] + [(i, val)] + arr[new_pos:]

    z = find(0, arr, f_value=True)

    key_a = arr[(z + 1000) % N][1]
    key_b = arr[(z + 2000) % N][1]
    key_c = arr[(z + 3000) % N][1]

    solution = key_a + key_b + key_c

    return solution


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = int(row.strip())
            input_.append(v)

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
