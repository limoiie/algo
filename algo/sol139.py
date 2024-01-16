from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_word_len = 0
        min_word_len = 20
        trie = Trie()
        for word in wordDict:
            max_word_len = max(max_word_len, len(word))
            min_word_len = min(min_word_len, len(word))
            trie.insert(word)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(max(i - max_word_len, 0), i - min_word_len + 1):
                if dp[j] and trie.search(s[j:i]):
                    dp[i] = True
        return dp[n]


class Trie:
    class Node:
        def __init__(self):
            self.children = {}

        def __getitem__(self, item):
            return self.children[item]

        def __setitem__(self, key, value):
            self.children[key] = value

        def __contains__(self, item):
            return item in self.children

    def __init__(self):
        self.root = self.Node()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = self.Node()
            node = node[c]
        node["$"] = None

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return "$" in node


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=("leetcode", ["leet", "code"]), expected=True),
    TestCase(args=("applepenapple", ["apple", "pen"]), expected=True),
    TestCase(args=("catsandog", ["cats", "dog", "sand", "and", "cat"]), expected=False),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.wordBreak(*case.args)
    assert output == case.expected
