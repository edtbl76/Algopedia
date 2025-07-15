class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev = prev

    def get_data(self):
        return self.data