class BinaryTree:

    def __init__(self, value):
        self.value  = value
        self.left = None
        self.right = None

    def add_node(self, value):

        if self.value == value:
            return

        if value < self.value:

            if self.left:
                self.left.add_node(value)
            else:
                self.left = BinaryTree(value)

        if value > self.value:

            if self.right:
                self.right.add_node(value)
            else:
                self.right = BinaryTree(value)

    def in_order_traversal(self):

        element = []

        if self.left:
            element += self.left.in_order_traversal()

        element.append(self.value)

        if self.right:
            element += self.right.in_order_traversal()

        return element


    def pre_order_traversal(self):

        element = []

        element.append(self.value)

        if self.left:
            element += self.left.pre_order_traversal()

        if self.right:
            element += self.right.pre_order_traversal()

        return element

    def post_order_traversal(self):
        element = []

        if self.left:
            element += self.left.post_order_traversal()

        if self.right:
            element += self.right.post_order_traversal()

        element.append(self.value)

        return element

    def find_min(self):

        min_value = self.value
        left_node = self.left

        while left_node:
            min_value = left_node.value
            left_node = left_node.left

        return min_value

    def find_max(self):

        max_value = self.value
        right_node = self.right

        while right_node:
            max_value = right_node.value
            right_node = right_node.right

        return max_value


if __name__ == "__main__":
    element = [1,2,3,4,5,6]
    root = BinaryTree(element[0])

    for i in range(1, len(element)):
        root.add_node(element[i])

    print(root.in_order_traversal())
    print(root.pre_order_traversal())
    print(root.post_order_traversal())
    print(root.find_min())
    print(root.find_max())



