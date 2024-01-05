from typing import List


class SegmentTree:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build_tree(arr, 0, 0, len(arr) - 1)

    def build_tree(self, arr, tree_idx, left, right):
        if left == right:
            self.tree[tree_idx] = arr[left]
            return

        mid = (left + right) // 2
        self.build_tree(arr, 2 * tree_idx + 1, left, mid)
        self.build_tree(arr, 2 * tree_idx + 2, mid + 1, right)
        self.tree[tree_idx] = self.tree[2 * tree_idx + 1] + self.tree[2 * tree_idx + 2]

    def update(self, arr_idx, new_val):
        self.update_tree(0, 0, len(self.arr) - 1, arr_idx, new_val)

    def update_tree(self, tree_idx, left, right, arr_idx, new_val):
        if left == right:
            self.tree[tree_idx] = new_val
            return

        mid = (left + right) // 2
        if arr_idx <= mid:
            self.update_tree(2 * tree_idx + 1, left, mid, arr_idx, new_val)
        else:
            self.update_tree(2 * tree_idx + 2, mid + 1, right, arr_idx, new_val)
        self.tree[tree_idx] = self.tree[2 * tree_idx + 1] + self.tree[2 * tree_idx + 2]

    def query(self, q_left, q_right):
        return self.query_tree(0, 0, len(self.arr) - 1, q_left, q_right)

    def query_tree(self, tree_idx, left, right, q_left, q_right):
        if q_left > right or q_right < left:
            return 0

        if q_left <= left and q_right >= right:
            return self.tree[tree_idx]

        mid = (left + right) // 2
        left_sum = self.query_tree(2 * tree_idx + 1, left, mid, q_left, q_right)
        right_sum = self.query_tree(2 * tree_idx + 2, mid + 1, right, q_left, q_right)
        return left_sum + right_sum
