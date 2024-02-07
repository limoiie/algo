def sol1(n: int, k: int):
    import fractions

    ep = fractions.Fraction(1, 1)
    op = fractions.Fraction(0, 1)

    for _ in range(n):
        ep, op = (
            ep * fractions.Fraction(k, k + 1) + op * fractions.Fraction(1, k + 1),
            op * fractions.Fraction(k, k + 1) + ep * fractions.Fraction(1, k + 1),
        )

    return (ep.numerator + ep.denominator) % 10


def test1():
    assert sol1(2, 5) == 1
    assert sol1(2, 6) == 6
    assert sol1(3, 7) == 9
    assert sol1(3, 9) == 9


def sol2(events: list[tuple[int, int]]):
    mod = 10**9 + 7

    first = True
    ans, acc = 0, 0
    i, n, l = 0, len(events), 2
    while i < n:
        j = l
        while j > 0 and i < n:
            m, b = events[i]
            if m < j:
                acc = (acc + m * b) % mod
                i += 1
                j -= m
            elif m > j:
                acc = (acc + j * b) % mod
                events[i] = (m - j, b)
                j = 0
            else:
                acc = (acc + m * b) % mod
                i += 1
                j = 0

        if i >= n:
            break

        ans = (ans + acc) % mod
        if not first:
            l += l
        first = True

    return ans


def test2():
    print(
        sol2(
            [
                (1, 1),
                (1, 2),
                (1, 3),
                (1, 4),
                (1, 5),
            ]
        )
    )


def sol3(h: int, a: int, h_list: list[int], a_list: list[int]):
    monsters = sorted(zip(h_list, a_list))

    dp = [1] * (len(monsters) + 1)
    for i, (hi, ai) in enumerate(monsters):
        for j, (hj, aj) in enumerate(monsters[:i]):
            if hi > hj and ai > aj:
                dp[i] = max(dp[i], dp[j] + 1)

    ans = 0
    for i, (hi, ai) in enumerate(monsters):
        if h > hi and a > ai:
            ans = max(ans, dp[i])

    return ans


def test3():
    print(
        sol3(
            4,
            5,
            [3, 3, 1],
            [3, 2, 1],
        )
    )


def sol4(n, projects: list[tuple[int, int, int, int]]):
    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))

        def union(self, x, y):
            self.parent[self.find(x)] = self.find(y)

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    selected, remaining = [], []
    uf = UnionFind(n + 1)
    for pi, (u, v, w, p) in enumerate(projects):
        if not p:
            remaining.append((w, u, v, pi))
            continue

        selected.append(pi)
        if uf.find(u) != uf.find(v):
            uf.union(u, v)

    remaining.sort()
    for w, u, v, pi in remaining:
        if uf.find(u) != uf.find(v):
            selected.append(pi)
            if len(selected) + 1 == n:
                break
            uf.union(u, v)

    return [pi + 1 for pi in selected]


def sol5(lines: list[list[int]]):
    points = []
    possible_cols = set()
    for line in lines:
        point = []
        for i, c in enumerate(line):
            if c == 1:
                point.append(i)
                possible_cols.add(i)
        points.append(list(reversed(point)))

    ans = 10**9
    for i in possible_cols:
        moves = 0
        for point in points:
            while len(point) > 1 and (abs(point[-2] - i) <= abs(point[-1] - i)):
                point.pop()

            moves += abs(point[-1] - i)
        ans = min(ans, moves)
    return ans


def test5():
    print(
        sol5(
            [
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
            ]
        )
    )


def sol01():
    pass


def test01():
    pass
