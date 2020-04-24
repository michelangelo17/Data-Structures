from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        '''Inserts the given value into the tree'''

        if self is None:
            self = BinarySearchTree(value)
        else:
            if self.value <= value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
            else:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)

    def contains(self, target):
        '''
        Returns True if the tree contains the value\n
        False if it does not
        '''

        found = False

        if self is None:
            return False

        if self.value == target:
            return True

        if self.value < target:
            if self.right is None:
                return False
            else:
                found = self.right.contains(target)

        if self.value > target:
            if self.left is None:
                return False
            else:
                found = self.left.contains(target)

        return found

    def get_max(self):
        '''Returns the maximum value found in the tree'''

        if self is None:
            return

        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        '''Calls the function `cb` on the value of each node'''

        if self is None:
            return
        else:
            cb(self.value)
            if self.right is not None:
                self.right.for_each(cb)

            if self.left is not None:
                self.left.for_each(cb)

    # DAY 2 Project -----------------------

    def in_order_print(self, node):
        '''Print all the values in order from low to high'''

        if node.left is not None:
            self.in_order_print(node.left)

        print(node.value)

        if node.right is not None:
            self.in_order_print(node.right)

    def bft_print(self, node):
        '''
        Print the value of every node, starting with the given node,\n
        in an iterative breadth first traversal
        '''

        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            cur_node = queue.storage.head.value
            queue.dequeue()
            if cur_node.left:
                queue.enqueue(cur_node.left)
            if cur_node.right:
                queue.enqueue(cur_node.right)
            print(cur_node.value)

    def dft_print(self, node):
        '''
        Print the value of every node, starting with the given node,\n
        in an iterative depth first traversal
        '''

        stack = Stack()
        stack.push(node)

        while stack.len() > 0:
            cur_node = stack.storage.head.value
            stack.pop()
            if cur_node.left:
                stack.push(cur_node.left)
            if cur_node.right:
                stack.push(cur_node.right)
            print(cur_node.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    def pre_order_dft(self, node):
        '''Print Pre-order recursive DFT'''

        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    def post_order_dft(self, node):
        '''Print Post-order recursive DFT'''

        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)
