def generator():
    tc, N = map(int, input().strip().split())
    table = dict()

    start = None
    for v in map(int, input().strip().split()):
        if start is None:
            start = v
        else:
            if str(start) in table:
                table[str(start)].append(str(v))
            else:
                table[str(start)] = str(v)
            start = None
    yield tc, table


def solve(table):
    


for _ in range(10):
    for tc, table in generator():
        print('#{} {}'.format(tc, solve(table)))