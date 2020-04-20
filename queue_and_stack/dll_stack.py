# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.len()

    def pop(self):
        if self.len() == 0:
            return
        return self.storage.remove_from_head()

    def len(self):
        self.size = self.storage.length
        return self.size
