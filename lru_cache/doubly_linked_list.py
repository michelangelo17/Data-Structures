"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_head = ListNode(value)
        if not self.head:
            self.head = new_head
            self.tail = new_head
        else:
            self.head.prev = new_head
            new_head.next = self.head
            self.head = new_head
        self.length += 1

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        new_tail = ListNode(value)
        if not self.head:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail
        self.length += 1
        return self.tail

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        if node is self.head or self.length == 1:
            return
        new_head = node.value
        self.delete(node)
        self.add_to_head(new_head)

    def move_to_end(self, node):
        if node is self.tail or self.length == 1:
            return
        new_tail = node.value
        self.delete(node)
        self.add_to_tail(new_tail)

    def delete(self, node):
        if self.length == 0:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return
        elif self.head is node:
            self.head = node.next
        elif self.tail is node:
            self.tail = node.prev
        node.delete()
        self.length -= 1

    def get_max(self):
        if self.length == 0:
            return
        elif self.length == 1:
            return self.head.value
        else:
            max_value = 0
            cur_node = self.head
            while cur_node is not None:
                if cur_node.value > max_value:
                    max_value = cur_node.value
                cur_node = cur_node.next
            return max_value
