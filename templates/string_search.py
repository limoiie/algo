def knuth_morris_pratt(s: str, p: str):
    """
    Knuth-Morris-Pratt algorithm

    Complexity
    ==========

    Time complexity:

    - Preprocessing O(m)

    - Matching O(n)

    Space complexity: O(m)

    Here, "n" represents the length of the string "s",
    and "m" represents the length of the string "p".

    :param s: Text
    :param p: Pattern
    :return: the index of the first occurrence of pattern in text, or -1 if not found
    """
    m, n = len(p), len(s)
    if m > n:
        return -1

    # Preprocess pattern
    lookup = [0] * m
    for i in range(1, m):
        k = lookup[i - 1]
        while k > 0 and p[k] != p[i]:
            k = lookup[k - 1]
        if p[k] == p[i]:
            k += 1
        lookup[i] = k

    # Match pattern
    k = 0
    for i in range(n):
        while k > 0 and p[k] != s[i]:
            k = lookup[k - 1]
        if p[k] == s[i]:
            k += 1
        if k == m:
            return i - m + 1
    return -1


def boyer_moore(s: str, p: str):
    """
    Boyer-Moore algorithm

    Complexity
    ==========

    Time complexity:

    - Preprocessing O(m + k)

    - Matching O(n)

    Space complexity: O(k)

    :param s: Text
    :param p: Pattern
    :return: the index of the first occurrence of pattern in text, or -1 if not found
    """

    def build_bad_char_table():
        lookup = [m] * 256
        for i in range(m - 1):
            lookup[ord(p[i])] = m - i - 1
        return lookup

    def build_good_suffix_table():
        lookup = [0] * m
        lookup[m - 1] = m
        j = 0
        for i in range(m - 2, -1, -1):
            if p[i] == p[m - 1 - j]:
                j += 1
            lookup[i] = j
        for i in range(m - 1):
            k = lookup[i]
            if k != 0:
                lookup[m - 1 - k] = min(k, lookup[m - 1 - k])
        return lookup

    def search():
        i = m - 1
        while i < n:
            j = m - 1
            while j >= 0 and s[i] == p[j]:
                i -= 1
                j -= 1
            if j < 0:
                return i + 1
            i += max(bad_char_table[ord(s[i])], good_suffix_table[j])
        return -1

    m, n = len(p), len(s)
    if m > n:
        return -1

    bad_char_table = build_bad_char_table()
    good_suffix_table = build_good_suffix_table()
    return search()


def rabin_karp(s: str, p: str):
    """
    Rabin-Karp algorithm

    Complexity
    ==========

    Time complexity:

    - Preprocessing O(m)

    - Matching
      - Average O(n)
      - Worst-case O(mn)

    Space complexity: O(1)

    :param s: Text
    :param p: Pattern
    :return: the index of the first occurrence of pattern in text, or -1 if not found
    """
    m, n = len(p), len(s)
    if m > n:
        return -1

    # Preprocessing
    base = 26
    p_hash, s_hash = 0, 0
    for i in range(m):
        p_hash = p_hash * base + ord(p[i])
        s_hash = s_hash * base + ord(s[i])

    # Matching
    power = base ** (m - 1)
    for i in range(n - m + 1):
        if p_hash == s_hash:
            if s[i : i + m] == p:
                return i
        if i < n - m:
            s_hash = (s_hash - ord(s[i]) * power) * base + ord(s[i + m])
    return -1
