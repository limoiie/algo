from algo import *


# leetcode submit region begin(Prohibit modification and deletion)
# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for h, k in people:
            ans.insert(k, (h, k))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


# noinspection PyPep8Naming,PyMethodMayBeStatic
class SolutionWithFenwickTree:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)

        max_h = 0
        groups = dict()
        for h, k in people:
            max_h = max(max_h, h)
            groups.setdefault(k, list()).append(h)

        buckets = []
        for k in sorted(groups.keys(), reverse=True):
            buckets.append((k, sorted(groups[k], reverse=True)))

        ans = []
        bit = FenwickTree(max_h + 1)
        for i in range(n):
            for k, bucket in buckets:
                if bucket and i - bit.query(bucket[-1]) == k:
                    h = bucket.pop()
                    ans.append([h, k])
                    bit.update(h, val=1)
                    break
        return ans


class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def query(self, i):
        """
        Query the sum of the first i (1-indexed) elements
        """
        acc = 0
        while i > 0:
            acc += self.tree[i]
            i -= i & -i
        return acc

    def update(self, i, val):
        """
        Update the value of the i-th element (0-indexed) by val
        """
        i += 1
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i


_cases = [
    TestCase(
        args=([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],),
        expected=[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.reconstructQueue(*case.args)
    assert output == case.expected
