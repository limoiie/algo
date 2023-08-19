import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurs = {}
        for i, c in enumerate(s):
            last_occurs[c] = i

        stack = []
        visited = set()
        for i, c in enumerate(s):
            if c in visited:
                continue

            while stack and stack[-1] > c and last_occurs[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(c)
            visited.add(c)

        return "".join(stack)


_cases = [
    (("bcabc",), "abc"),
    (("cbacdcbc",), "acdb"),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol316(inputs, expected):
    sol = Solution()
    output = sol.removeDuplicateLetters(*inputs)
    assert output == expected
