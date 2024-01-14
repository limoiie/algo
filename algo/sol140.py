from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    dp: Dict[str, List[str]]
    trie: "Trie"

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.dp = defaultdict(list)
        self.trie = Trie(wordDict)
        self.backtrace(s, 0)
        return [" ".join(path) for path in self.dp[s]]

    def backtrace(self, s: str, starting) -> List[str]:
        if starting >= len(s):
            return [[]]

        if s[starting:] in self.dp:
            return self.dp[s[starting:]]

        for j in range(starting, len(s)):
            if s[starting : j + 1] in self.trie:
                for sentence in self.backtrace(s, j + 1):
                    self.dp[s[starting:]].append([s[starting : j + 1]] + sentence)

        return self.dp[s[starting:]]


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

    def add(self, word: str):
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
        expected=["cat sand dog", "cats and dog"],
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.wordBreak(*case.args)
    assert output == case.expected
