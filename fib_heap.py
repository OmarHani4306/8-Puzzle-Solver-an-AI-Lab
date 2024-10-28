import math

class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.mark = False
        self.left = self
        self.right = self

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.num_nodes = 0

    def is_empty(self):
        return self.min_node is None

    def insert(self, key):
        node = FibonacciHeapNode(key)
        if self.min_node is None:
            self.min_node = node
        else:
            node.left = self.min_node
            node.right = self.min_node.right
            self.min_node.right.left = node
            self.min_node.right = node
            if node.key < self.min_node.key:
                self.min_node = node
        self.num_nodes += 1
        return node

    def minimum(self):
        if self.min_node is None:
            return None
        return self.min_node.key

    def merge(self, other_heap):
        if other_heap is None or other_heap.min_node is None:
            return

        if self.min_node is None:
            self.min_node = other_heap.min_node
        else:
            # Merge the root lists
            self.min_node.right.left = other_heap.min_node.left
            other_heap.min_node.left.right = self.min_node.right
            self.min_node.right = other_heap.min_node
            other_heap.min_node.left = self.min_node

            if other_heap.min_node.key < self.min_node.key:
                self.min_node = other_heap.min_node

        self.num_nodes += other_heap.num_nodes

    def _remove_from_root_list(self, node):
        if node == node.right:
            self.min_node = None
        else:
            node.left.right = node.right
            node.right.left = node.left
            if node == self.min_node:
                self.min_node = node.right

    def _link(self, node1, node2):
        self._remove_from_root_list(node2)
        node2.left = node2.right = node2
        node2.parent = node1
        if node1.child is None:
            node1.child = node2
        else:
            node2.left = node1.child
            node2.right = node1.child.right
            node1.child.right = node2
            node2.right.left = node2
        node1.degree += 1
        node2.mark = False

    def _consolidate(self):
        max_degree = int(math.log2(self.num_nodes)) + 1
        degree_table = [None] * (max_degree + 1)

        nodes = [node for node in self._iterate(self.min_node)]

        for current in nodes:
            degree = current.degree
            while degree_table[degree] is not None:
                other = degree_table[degree]
                if current.key > other.key:
                    current, other = other, current
                self._link(current, other)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = current

        self.min_node = None
        for node in degree_table:
            if node is not None:
                if self.min_node is None:
                    self.min_node = node
                    node.left = node.right = node
                else:
                    node.left = self.min_node
                    node.right = self.min_node.right
                    self.min_node.right.left = node
                    self.min_node.right = node
                    if node.key < self.min_node.key:
                        self.min_node = node

    def extract_min(self):
        min_node = self.min_node
        if min_node is not None:
            if min_node.child is not None:
                children = [child for child in self._iterate(min_node.child)]
                for child in children:
                    child.parent = None
                    self.min_node.left.right = child
                    child.left = self.min_node.left
                    child.right = self.min_node
                    self.min_node.left = child

            self._remove_from_root_list(min_node)
            if min_node == min_node.right:
                self.min_node = None
            else:
                self.min_node = min_node.right
                self._consolidate()

            self.num_nodes -= 1
        return min_node

    def _cut(self, node, parent):
        if node == node.right:
            parent.child = None
        else:
            node.left.right = node.right
            node.right.left = node.left
            if node == parent.child:
                parent.child = node.right
        parent.degree -= 1
        self.min_node.left.right = node
        node.left = self.min_node.left
        node.right = self.min_node
        self.min_node.left = node
        node.parent = None
        node.mark = False

    def _cascade_cut(self, node):
        parent = node.parent
        if parent is not None:
            if not node.mark:
                node.mark = True
            else:
                self._cut(node, parent)
                self._cascade_cut(parent)

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key is greater than current key.")
        node.key = new_key
        parent = node.parent
        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._cascade_cut(parent)
        if node.key < self.min_node.key:
            self.min_node = node

    def delete(self, node):
        self.decrease_key(node, float('-inf'))
        self.extract_min()

    def _iterate(self, start):
        current = stop = start
        while True:
            yield current
            current = current.right
            if current == stop:
                break



if __name__ == "__main__":
    heap = FibonacciHeap()

    heap.insert((3, 2))
    heap.insert((2, 3))
    heap.insert((1, 1))  
    # node1 = heap.insert(3)
    # node2 = heap.insert(5)
    # node3 = heap.insert(1)
    # node4 = heap.insert(9)
    # node5 = heap.insert(7)
    # print('the heap: {}'.format(heap.trees))

    print('the minimum value of the fibonacci heap: {}'.format(heap.minimum()))

    print('the minimum value removed: {}'.format(heap.extract_min().key))