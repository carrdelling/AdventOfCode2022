from collections import deque


def solve(data):

    ROUNDS = 10000

    common_index = 1
    for m in data:
        common_index *= m[3]

    for r in range(ROUNDS):
        for idx in range(len(data)):
            while len(data[idx][1]) > 0:
                data[idx][-1] += 1
                item = data[idx][1].popleft()
                if data[idx][2][0] == '+':
                    item += data[idx][2][1]
                elif data[idx][2][0] == '*':
                    item *= data[idx][2][1]
                elif data[idx][2][0] == '^':
                    item *= item
                dest = data[idx][4] if item % data[idx][3] == 0 else data[idx][5]
                data[dest][1].append(item % common_index)

    monkey_business = sorted([x[-1] for x in data], reverse=True)
    solution = monkey_business[0] * monkey_business[1]
    return solution


def main():

    input_ = []
    idx = -1
    with open('input') as in_f:
        for row in in_f:

            if 'Monkey' in row:
                idx += 1
            if 'Starting items' in row:
                items = row.strip().split(': ')[-1].split(', ')
                items = deque(list(map(int, items)))
            if 'Operation' in row:

                if 'old * old' in row:
                    op = ('^', 1)
                elif '+' in row:
                    v = int(row.strip().split(' ')[-1])
                    op = ('+', v)
                elif '*' in row:
                    v = int(row.strip().split(' ')[-1])
                    op = ('*', v)

            if 'Test' in row:
                test = int(row.strip().split(' ')[-1])

            if 'If true:' in row:
                dest_true = int(row.strip().split(' ')[-1])
            if 'If false:' in row:
                dest_false = int(row.strip().split(' ')[-1])

                # build the monkey
                monkey_business = 0

                monkey = [idx, items, op, test, dest_true, dest_false, monkey_business]
                input_.append(monkey)

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
