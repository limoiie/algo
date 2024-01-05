class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, start, end):
        if not self.root:
            self.root = IntervalNode(start, end)
        else:
            self.root.insert(start, end)

    def search(self, start, end):
        if self.root:
            return self.root.search(start, end)
        return []


class IntervalNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def insert(self, start, end):
        if start <= self.start:
            if not self.left:
                self.left = IntervalNode(start, end)
            else:
                self.left.insert(start, end)
        else:
            if not self.right:
                self.right = IntervalNode(start, end)
            else:
                self.right.insert(start, end)

    def search(self, start, end):
        result = []
        if start <= self.end and end >= self.start:
            result.append((self.start, self.end))
        if self.left and start <= self.left.end:
            result.extend(self.left.search(start, end))
        if self.right and end >= self.right.start:
            result.extend(self.right.search(start, end))
        return result
