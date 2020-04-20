# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.len()

    def dequeue(self):
        if self.len() == 0:
            return
        return self.storage.remove_from_head()

    def len(self):
        self.size = self.storage.length
        return self.size
