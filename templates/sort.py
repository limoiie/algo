from typing import *


def quick_select(nums: List[int], l: int, r: int, k: int):
    """
    Partially sort nums such that:
    1. nums[:k] <= nums[k - 1] <= nums[k:], indicating
      the first k elements are not larger than the last n-k elements of nums.
    2. nums[k] is equal to sorted(nums)[k], meaning
      the (k-1)-th element of nums is the (k-1)-th element in the final sorted nums.

    This algorithm can be used to:
    -  Retrieve the k-th element from an unsorted list in any order.
    -  Retrieve the top-k elements from an unsorted list in any order.
    """
    if not (0 < k <= r - l + 1):
        return None

    i = two_way_partition(nums, l, r - 1, nums[r])
    nums[i], nums[r] = nums[r], nums[i]

    if i - l == k - 1:
        return nums[k]

    if i - l > k - 1:
        return quick_select(nums, l, i - 1, k)
    return quick_select(nums, i + 1, r, k - i + l - 1)


def two_way_partition(nums: List[int], l, r, pivot):
    """
    In-place partition nums into two parts, so that:
    - Finally:
      - A[:i] <= pivot < A[i:], meaning
        the first i elements are less than the last n-i elements of nums
    """
    i, j, k = l, l, r - 1
    while j <= k:
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        else:
            j += 1

    return i


def three_way_partition(nums: List[int], l, r, pivot: int):
    """
    In-place partition nums into three parts, so that:
    - Runtime:
      - A[:i] < pivot = A[i:j] < A[k + 1:]
    - Finally:
      - A[:i] < pivot = A[i:j] < A[j:]
    """
    i, j, k = l, l, r - 1
    while j <= k:
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[j] > pivot:
            nums[k], nums[j] = nums[k], nums[i]
            k -= 1
        else:
            j += 1

    return i, j


def merge_sort_in_place(nums: List[int], l: int, r: int):
    """
    In-place merge sort nums[l:r] in ascending order.
    """
    if l >= r:
        return

    m = (l + r) >> 1
    merge_sort_in_place(nums, l, m)
    merge_sort_in_place(nums, m, r)

    merge(nums, l, m, r)


def merge(nums: List[int], l: int, m: int, r: int):
    """
    Merge nums[l:m] and nums[m:r] in ascending order.
    """
    i, j = l, m
    while i < m and j < r:
        if nums[i] <= nums[j]:
            i += 1
        else:
            nums[i], nums[i + 1 : j + 1] = nums[j], nums[i:j]
            i, j, m = i + 1, j + 1, m + 1


def merge_sort_based(nums: List[int], l: int, r: int):
    if l >= r:
        return ...

    m = (l + r) >> 1
    merge_sort_based(nums, l, m)
    merge_sort_based(nums, m, r)

    ...  # compute properties from the sorted nums[l:m] and nums[m:r]

    merge(nums, l, m, r)
    return ...
