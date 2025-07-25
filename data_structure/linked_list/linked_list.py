from os import times_result
from timeit import timeit

from data_structure.Nodes import LinkedListNode


class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):

        if not self.head:
            return "empty linked list"

        list_values = []
        pointer = self.head

        while pointer:
            list_values.append(str(pointer.value))
            pointer = pointer.next_node

        return "-->".join(list_values)

    def append(self, data):

        if not self.head:
            self.head = LinkedListNode(data, None)

        else:
            pointer = self.head
            while pointer.next_node:
                pointer = pointer.next_node
            pointer.next_node = LinkedListNode(data, None)
        return

    def pop(self):

        if not self.head:
            return

        pointer = self.head
        last_node = None
        while pointer.next_node:
            last_node = pointer
            pointer = pointer.next_node
        if not last_node:
            self.head = None
        else:
            last_node.next_node = None
        return None

    def insert(self, data, index):

        if not self.head and index > 0:
            raise IndexError("index out of range")

        pointer = self.head
        cur = None
        next = None
        while index and pointer:
            cur = pointer
            next = pointer.next_node
            pointer = pointer.next_node
            index -= 1
        if cur and next:
            node = LinkedListNode(data, next)
            cur.next_node = node
        else:
            raise IndexError("index out of range")
        return

    def delete(self, index):

        if not self.head and index > 0:
            raise IndexError("index out of range")

        pointer = self.head
        cur = None
        last_node = None
        while index > 0 and pointer.next_node:
            last_node = pointer
            cur = pointer.next_node
            pointer = pointer.next_node
            index -= 1
        if index != 0:
            raise IndexError("index out of range")
        if last_node and cur:
            last_node.next_node = cur.next_node
        else:
            raise IndexError("index out of range")
        return


if __name__ == "__main__":
    pass
