from collections import defaultdict
from functools import lru_cache


def solve(data):

    tree = defaultdict(set)
    parents = {}
    files = defaultdict(set)

    location = '/'

    for command in data[1:]:

        if command.startswith('$'):
            if command.startswith('$ ls'):
                pass
            else:
                name = command[5:]

                if name == '..':
                    location = '/'.join(location.split('/')[:-1])
                else:
                    location = f"{location}/{name}"

        else:
            if command.startswith('dir'):
                name = f"{location}/{command[4:]}"
                tree[location].add(name)
                parents[name] = location
            else:
                size, name = command.split()
                files[location].add((name, int(size)))

    @lru_cache
    def _folder_size(folder):

        _size = sum(f[1] for f in files[folder])
        for f in tree[folder]:
            _size += _folder_size(f)

        return _size

    sizes = {f: _folder_size(f) for f in parents}
    sizes['/'] = _folder_size('/')

    solution = sum(s for s in sizes.values() if s <= 100000)

    return solution


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = row.strip()
            input_.append(v)
            
    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()


