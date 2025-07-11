from data_structures.Node import Node


class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)

    def get_head(self):
        return self.head

    def insert_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def stringify_list(self):
        string_list  = ""
        current_node = self.get_head()
        while current_node:
            if current_node.get_data() is not None:
                string_list += str(current_node.get_data()) + "\n"
            current_node = current_node.next
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head()
        if current_node.get_data() is value_to_remove:
            self.head = current_node.get_next()
        else:
            while current_node and current_node.get_next():
                next_node = current_node.get_next()
                if next_node.get_data() is value_to_remove:
                    current_node.set_next(next_node.get_next())
                    current_node = None
                else:
                    current_node = next_node
