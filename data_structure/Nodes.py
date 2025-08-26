class LinkedListNode:

    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class TreeNode:

    def __init__(self, value, parent):

        self.value = value
        self.parent = parent
        self.children = []
