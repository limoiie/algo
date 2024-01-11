# Algo

## Data Structures

[](https://stackoverflow.com/questions/17466218/what-are-the-differences-between-segment-trees-interval-trees-binary-indexed-t)

- [ ] Heap

- [ ] Tree, Binary Tree, Binary Search Tree
  - Balance BST
    - [ ] Day-Stout-Warren Algorithm - reduce height to O(log n)

- [ ] Binary Indexed Tree

- [ ] Segment Tree

- [ ] Interval Tree

- [ ] Range Tree

- [x] Disjoint (Union-Find) Set
  - to find circle
  - to find strong connection component 
    - [LC 827](https://leetcode.com/problems/making-a-large-island/)
  - to find spanning tree
  - to cluster by connection
    - [LC 839](https://leetcode.com/problems/similar-string-groups/)
  - to compute bipartite
    - [LC 886](https://leetcode.com/problems/possible-bipartition/)

- [ ] Suffix Array

- [ ] Trie

## Algorithms

### Search

- [ ] Binary Search

- [ ] Depth-First Search

- [ ] Breadth-First Search

### Enumeration

- [ ] Enumerate primes

- [ ] Ugly number (2,3,5)

- [ ] N-th ugly number (2,3,5)

### General

- [ ] Brute Force

- [ ] Divide and Conquer

- [ ] Dynamic Programming

- [ ] Greedy

### Sort

- [ ] Quick Sort

- [ ] Merge Sort

- [ ] Heap Sort

- [ ] Counting Sort

- [ ] Radix Sort

- [ ] Bucket Sort

- [ ] Topological Sort

### Graph

- [ ] Shortest Path

- [ ] Minimum-Spanning Tree

- [ ] Network Flow

- [ ] Bipartite Matching

- [ ] Strongly Connected Component

- [ ] Biconnected Component

- [ ] Eulerian (Circuit) Path

- [ ] Hamiltonian Path

### KMP

### Math

## Python Standard Library

### `bisect` for Binary Search

[bisect](https://docs.python.org/3/library/bisect.html)

- `bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)`
    - The returned insertion point `i`
      partitions the array `a` into two halves
      so that `all(val < x for val in a[lo : i])` for the left side
      and `all(val >= x for val in a[i : hi])` for the right side.
- `bisect.bisect_right(a, x, lo=0, hi=len(a), *, key=None)`
    - The returned insertion point `i` partitions
      the array `a` into two halves
      so that `all(val <= x for val in a[lo : i])` for the left side
      and `all(val > x for val in a[i : hi])` for the right side.
- `bisect.insort_left(a, x, lo=0, hi=len(a), *, key=None)`
    - Insert `x` in `a` at point returned by `bisect.bisect_left`
      in sorted order.
- `bisect.insort_right(a, x, lo=0, hi=len(a), *, key=None)`
    - Insert `x` in `a` at point returned by `bisect.bisect_right`
      in sorted order.

### `collections` for Data Structures

[collections](https://docs.python.org/3/library/collections.html)

- `collections.deque([iterable[, maxlen]])`
    - [deque](https://docs.python.org/3/library/collections.html#deque-objects)
    - Returns a new deque object initialized left-to-right
      (using `append()`) with data from `iterable`.

### `heapq` for Heap Operation

[heapq](https://docs.python.org/3/library/heapq.html).

- `heapq.heappush(heap, item)`
    - Push the value item onto the heap, maintaining the heap invariant.

- `heapq.heappop(heap)`
    - Pop and return the smallest item from the heap,
      maintaining the heap invariant.

- `heapq.heappushpop(heap, item)`
    - Push item on the heap, then pop and return the smallest item
      from the heap. The combined action runs more efficiently
      than `heappush()` followed by a separate call to `heappop()`.

- `heapq.heapify(x)`
    - Transform list `x` into a heap, in-place, in linear time.

- `heapq.heapreplace(heap, item)`
    - Pop and return the smallest item from the heap,
      and also push the new item.
    - The heap size does not change.
      If the heap is empty, `IndexError` is raised.
      This is more efficient than `heappop()` followed by `heappush()`,
      and can be more appropriate when using a fixed-size heap.
      The pop/push combination always returns an element from the heap
      and replaces it with `item`.
      The value returned may be larger than the item added.

- `heapq.merge(*iterables, key=None, reverse=False)`
    - Merge multiple sorted inputs into a single sorted output
      (for example, merge timestamped entries from multiple log files).
      Returns an iterator over the sorted values.

- `heapq.nlargest(n, iterable, key=None)`
    - Return a list with the `n` largest elements from the dataset
      defined by `iterable`.

- `heapq.nsmallest(n, iterable, key=None)`
    - Return a list with the `n` smallest elements from the dataset
      defined by `iterable`.
