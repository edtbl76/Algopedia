from data_structures.SinglePointNode import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):

        if self.has_space():
            added = Node(value)

            if self.is_empty():
                self.head = added
                self.tail = added
            else:
                self.tail.next = added
                self.tail = added

            self.size += 1

    def dequeue(self):

        if not self.is_empty():
            removed = self.head

            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = removed.next

            self.size -= 1

            return removed.data

        else:
            return None

    def peek(self):
        return self.head.data

    def get_size(self):
        return self.size

    def has_space(self):
        return self.max_size is None or self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0
