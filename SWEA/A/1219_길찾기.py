def generator():
    table = dict()
    tc, N = map(int, input().strip().split())

    start = None
    for v in map(int, input().strip().split()):
        if start is None:
            start = v
        else:
            if str(start) in table:
                table[str(start)].append(str(v))
            else:
                table[str(start)] = [str(v)]
            start = None
    yield tc, table


def solve(table):
    visited = [False] * 100
    next_pos = table['0'] # queue
    while next_pos:
        pos = next_pos.pop()

        # Check visited city
        if visited[int(pos)]:
            continue
        else:
            # If not visited, check linked cities
            add_next_pos = []
            if pos in table:
                add_next_pos = table[pos]
            # Check if '99' city is in next city's List
            if '99' in add_next_pos:
                return 1
            next_pos.extend(add_next_pos)
    return 0


for _ in range(10):
    for tc, table in generator():
        print('#{} {}'.format(tc, solve(table)))