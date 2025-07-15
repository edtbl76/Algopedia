from data_structures.SinglePointNode import Node


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


    def swap_node(self, value1, value2):
        node1 = self.get_head()
        node2 = self.get_head()
        node1_prev = None
        node2_prev = None

        # short circuit
        if value1 is value2:
            return

        # find match 1
        while node1 is not None:
            if node1.get_data() is value1:
                break
            node1_prev = node1
            node1 = node1.get_next()

        # find match 2
        while node2 is not None:
            if node2.get_data() is value2:
                break
            node2_prev = node2
            node2 = node2.get_next()

        # make sure the elements are in the list
        if node1 is None or node2 is None:
            return

        # update preceding node's pointers
        if node1_prev is None:
            self.head = node2
        else:
            node1_prev.set_next(node2)

        if node2_prev is None:
            self.head = node1
        else:
            node2_prev.set_next(node1)

        # Update pointers
        temp = node1.get_next()
        node1.set_next(node2.get_next())
        node2.set_next(temp)

    # list nth last v1 (naive)
    #
    def list_nth_last_dual_list(self, n):
        # gets the nth element from the tail of the list.

        # stores an entire representation of the list
        # PRO -- easy to read
        # CON -- wastes memory

        ll_as_list = []
        current_node = self.head

        while current_node:
            ll_as_list.append(current_node)
            current_node = current_node.get_next()
        return ll_as_list[len(ll_as_list) - n]

    # list nth last v2 (parallel pointers)
    # - parallel pointers are useful unless you have to find the middle or other elements that
    # - might waste space
    #
    def list_nth_last_parallel_pointers(self, n):
        # gets the nth element from the tail of the list.

        # improved impl. because it uses 2 pointers moving at the same rate
        # "tail pointer" moves n steps behind the first one.
        current_node = None
        tail_pointer = self.head
        count = 1

        # We'll iterate as long as the tail_pointer isn't None (i.e. it moves through the entire data structure)
        while tail_pointer:
            tail_pointer = tail_pointer.get_next()
            count += 1

            # Once the counter reaches n + 1, the second pointer enters the algorithm (n steps behind).
            if count >= n + 1:
                # if this is the introduction of the pointer, then init. it to the head of the structure.
                # otherwise, move it to the next Node.
                if current_node is None:
                    current_node = self.head
                else:
                    current_node = current_node.get_next()

        # Once tail_pointer reaches None, we've cycled through the entire structure and N should be positioned at
        # the stop condition.
        return current_node


    # Moving 1 pointer at 2x speed as the other allows us to find the middle.
    # - once the fast pointer reaches the end, the slow pointer is at the middle.
    #
    def find_middle(self):
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer:
            # (additional step, so that fast_pointer moves at 2x speed)
            fast_pointer = fast_pointer.get_next()
            if fast_pointer:
                fast_pointer = fast_pointer.get_next()
                slow_pointer = slow_pointer.get_next()
        return slow_pointer


    # Alternate solution
    # this version of find_middle is harder to read and uses a ctr var so we move on odd loops only
    def find_middle_half(self):
        count = 0
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer:
            fast_pointer = fast_pointer.get_next()
            if count % 2 != 0:
                slow_pointer = slow_pointer.get_next()
            count += 1
        return slow_pointer
