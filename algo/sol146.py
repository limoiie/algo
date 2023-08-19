# noinspection PyUnresolvedReferences
from typing import *

import pytest


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class LRUCache:
    def __init__(self, capacity):
        self.size = capacity
        self.m = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, new_node):
        temp = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = temp
        temp.prev = new_node

    def move_to_front(self, node):
        node.delete()
        self.add_node(node)
        return self.head.next

    def get(self, key):
        if key not in self.m:
            return -1

        self.m[key] = self.move_to_front(self.m[key])
        return self.head.next.val

    def put(self, key, value):
        if key in self.m:
            self.m[key].val = value
            self.m[key] = self.move_to_front(self.m[key])
        else:
            if len(self.m) == self.size:
                prev = self.tail.prev
                prev.delete()
                l = Node(key, value)
                self.add_node(l)
                del self.m[prev.key]
                self.m[key] = self.head.next
            else:
                l = Node(key, value)
                self.add_node(l)
                self.m[key] = self.head.next


_cases = [
    ((),),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol146(inputs, expected):
    pass
