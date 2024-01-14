from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    trie: "Trie"
    ans: Set[str]
    m: int
    n: int

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.m, self.n = len(board), len(board[0])
        self.trie = Trie(words)

        self.ans = set()
        visited = [[False] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.backtrace(board, visited, (i, j), [], self.trie.root)
        return list(self.ans)

    def backtrace(self, board, visited, starting, path, node):
        x, y = starting
        if board[x][y] not in node.children:
            return
        node = node.children[board[x][y]]

        path.append(board[x][y])
        visited[x][y] = True
        if node.is_word:
            self.ans.add("".join(path))
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.m and 0 <= ny < self.n and not visited[nx][ny]:
                self.backtrace(board, visited, (nx, ny), path, node)
        visited[x][y] = False
        path.pop()


class Trie:
    class Node:
        def __init__(self, is_word=False):
            self.children = defaultdict(Trie.Node)
            self.is_word = is_word

        def __contains__(self, item):
            return item in self.children

    def __init__(self, words: List[str] = None):
        self.root = Trie.Node()
        if words:
            for word in words:
                self.add(word)

    def __contains__(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr.children[c]
        return curr.is_word

    def add(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(["oaan", "etae", "ihkr", "iflv"], ["oath", "pea", "eat", "rain"]),
        expected=["eat", "oath"],
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.findWords(*case.args)
    assert output == case.expected
