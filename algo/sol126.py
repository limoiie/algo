from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        word_set.add(beginWord)
        word_dict = defaultdict(list)
        for word in word_set:
            for i in range(len(word)):
                word_dict[word[:i] + "." + word[i + 1 :]].append(word)

        n_steps = 0
        visited, adj = defaultdict(int), defaultdict(list)
        visited[beginWord] = 0
        queue = deque([(beginWord, n_steps)])
        while queue:
            word, n_steps = queue.popleft()
            if word == endWord:
                break
            for i in range(len(word)):
                pat = word[:i] + "." + word[i + 1 :]
                for next_word in word_dict.get(pat, []):
                    if next_word not in visited or visited[next_word] == n_steps + 1:
                        adj[next_word].append(word)
                        if next_word not in visited:
                            queue.append((next_word, n_steps + 1))
                            visited[next_word] = n_steps + 1

        if n_steps == 0:
            return []

        result = []
        self.backtrace([endWord], n_steps, beginWord, adj, result)
        return result

    def backtrace(self, path, step, beginWord, adj, result):
        if step == 0:
            if path[-1] == beginWord:
                result.append(path[::-1])
            return

        for neighbor in adj[path[-1]]:
            path.append(neighbor)
            self.backtrace(path, step - 1, beginWord, adj, result)
            path.pop()


def is_adjacent(left, right):
    cnt = 0
    for l, r in zip(left, right):
        cnt += l != r
    return cnt == 1


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log", "cog"],
        ),
        expected=[
            ["hit", "hot", "dot", "dog", "cog"],
            ["hit", "hot", "lot", "log", "cog"],
        ],
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.findLadders(*case.args)
    assert output == case.expected
