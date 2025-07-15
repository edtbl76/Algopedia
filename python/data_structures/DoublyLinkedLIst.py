from data_structures.TwoPointNode import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert new node at head of list
    def insert(self, value):
        new_head = Node(value)
        current_head = self.head

        if current_head is not None:
            current_head.set_prev(new_head)
            new_head.set_next(current_head)

        self.head = new_head

        if self.tail is None:
            self.tail = new_head

    # Insert new node at tail of list
    def append(self, value):
        new_tail = Node(value)
        current_tail = self.tail

        if current_tail is not None:
            current_tail.set_next(new_tail)
            new_tail.set_prev(current_tail)

        self.tail = new_tail

        if self.head is None:
            self.head = new_tail


    def remove_head(self):
        removed = self.head

        if removed is None:
            return None

        self.head = removed.get_next()

        if self.head is not None:
            self.head.set_prev(None)

        if removed == self.tail:
            self.remove_tail()

        return removed.get_data()

    def remove_tail(self):
        removed = self.tail

        if removed is None:
            return None

        self.tail = removed.get_prev()

        if self.tail is not None:
            self.tail.set_next(None)

        if removed == self.head:
            self.remove_head()

        return removed.get_data()


    def remove_node_by_value(self, value):
        removed = None

        current_node = self.head

        while current_node is not None:

            if current_node.get_data() == value:
                removed = current_node
                break

            current_node = current_node.get_next()

        if removed is None:
            return None

        if removed == self.head:
            self.remove_head()
        elif removed == self.tail:
            self.remove_tail()
        else:
            removed_next = removed.get_next()
            removed_prev = removed.get_prev()
            removed_next.set_prev(removed_prev)
            removed_prev.set_next(removed_next)

        return removed


    def stringify(self):
        string_list = ""
        current_node = self.head
        while current_node:
            if current_node.get_data() is not None:
                string_list += str(current_node.get_data()) + "\n"
            current_node = current_node.get_next()
        return string_list

