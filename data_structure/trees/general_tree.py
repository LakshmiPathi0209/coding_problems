class GeneralTree():

    def __init__(self, value):
        self.value = value
        self.children = []
        self.perant = None

    def add_child(self, child_node):
        child_node.perant = self
        self.children.append(child_node)

    def get_level(self):
        level = 0
        p = self.perant
        while p:
            level += 1
            p = p.perant
        return level

    def print_tree(self):

        prefix = self.get_level() * "|--"
        print(f'{prefix}{self.value}')
        if self.children:

            for child in self.children:
                child.print_tree()


if __name__ == "__main__":

    root = GeneralTree("electronics")

    laptop_node = GeneralTree("laptops")
    laptop_node.add_child(GeneralTree("mac"))
    laptop_node.add_child(GeneralTree("asus"))
    laptop_node.add_child(GeneralTree("ROG"))

    mobile_node = GeneralTree("mobile")
    mobile_node.add_child(GeneralTree("samsung"))
    mobile_node.add_child(GeneralTree("apple"))
    mobile_node.add_child(GeneralTree("moto"))

    tv_node = GeneralTree("Tv")
    tv_node.add_child(GeneralTree("realme"))
    tv_node.add_child(GeneralTree("onida"))
    tv_node.add_child(GeneralTree("lg"))

    root.add_child(laptop_node)
    root.add_child(mobile_node)
    root.add_child(tv_node)

    root.print_tree()

