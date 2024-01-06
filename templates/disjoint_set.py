class UnionFind:
    """
    UnionFind,
    also known as a disjoint-set data structure or merge-find set,
    is a data structure used in computer science.

    It stores a collection of disjoint sets
    and allows for operations such as adding new sets, merging sets,
    and finding a representative member of a set.

    One common implementation is called a disjoint-set forest,
    which performs unions and finds in near-constant amortized time.
    Union-find data structures are used in algorithms
    like Kruskal's algorithm for finding minimum spanning trees
    and have applications in symbolic. [^1]

    [^1]: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    """

    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        self.parent[root_x] = root_y


class RankUnionFind:
    """
    UnionFind with rank,
    where the rank of a tree is the height of the tree.

    The functionality of RankUnionFind is no different from UnionFind,
    except that
    RankUnionFind tries to reduce the cost of find
    by tracing the height of the tree.
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y

        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x

        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


class CountUnionFind:
    """
    UnionFind with counting for each root,
    where the counting of a tree is the size of the tree.

    The functionality of CountUnionFind is no different from UnionFind,
    except that
    CountUnionFind tries to maintain the size
    for each root of the tree.
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.count = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        self.parent[root_x] = root_y
        self.count[root_y] += self.count[root_x]
