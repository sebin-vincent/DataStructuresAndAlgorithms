class BinaryTree:
    def __init__(self, root):
        self.__root = self.Node(1)

    class Node:
        def __init__(self, data, left=None, right=None):
            self.left = left
            self.right = right
            self.data = data

    def add_node(self, data):
        new_node = self.Node(data)
        if self.__root is None:
            self.__root = new_node
        else:
            self.find_node_pos(self.__root, data, new_node)

    def find_node_pos(self, root, data, new_node):
        if data >= root.data:
            if root.right is None:
                root.right = new_node
                return
            else:
                return self.find_node_pos(root.right, data, new_node)
        else:
            if root.left is None:
                root.left = new_node
                return
            else:
                self.find_node_pos(root.left, data, new_node)

    def search_node(self, data):
        return self.find_node(self.__root, data)

    def find_node(self, root, data):
        if root is None:
            return 0
        if data > root.data:
            return self.find_node(root.right, data)
        elif data < root.data:
            return self.find_node(root.left, data)
        else:
            return root


tree = BinaryTree(2)
tree.add_node(3)
tree.add_node(1)

