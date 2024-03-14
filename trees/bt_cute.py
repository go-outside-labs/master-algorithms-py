#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


class SimpleTree:
    """Implementation of a simple tree"""

    def __init__(self, value=None, node=None):
        self.value = value
        self.node = node or []
        
    def __repr__(self, level=0):
        repr = '\t' * level  + self.value + '\n'
        for n in self.node:
            repr += n.__repr__(level + 1)
        return repr


class Node():
    """Implementation of a Node for a binary tree"""

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    ############################
    #       Private Methods
    ############################
    def __repr__(self):
        """Prints the node"""
        return f'{self.value}'

    def _repr_preorder(self):
        """Prints the tree in preorder traversal (root, left, right)"""

        print(self.value)
        if self.left:
            self.left._repr_preorder()
        if self.right:
            self.right._repr_preorder()
    
    def _add_node_binary_tree(self, value):
        """Adds a node to a simple binary tree"""

        if self.value is None:
            self.value = value
        
        else:
            if not self.left:
                self.left = Node(value)
            elif not self.right:
                self.right = Node(value)
            else:
                self.left = self.left._add_node_binary_tree(value)

        return self
    
    def _add_node_binary_search_tree(self, value) -> bool:
        """Adds a node to a binary search tree"""

        if not self.value:
            self.value = value

        else:
            new_node = Node(value)
            if value < self.value:
                self.left = self.left and self.left._add_node_binary_search_tree(value) or new_node
            elif value > self.value:
                self.right = self.right and self.right._add_node_binary_search_tree(value) or new_node
            else:
                print(f'❌ Item {value} not added as BSTs do not support repetition.')
        
        return self

    def _search_node_preorder(self, query) -> bool:
        """Searches through preorder traversal (node, left, right)"""

        if self.value == query:
            return True
       
        found = False
        if self.left:
            # recursively search left
            found = self.left._search_node_preorder(query)
        
        if self.right:
            # recursively search right
            found = found or self.right._search_node_preorder(query)
        
        return found

    def _search_node_binary_search_tree(self, query) -> bool:
        """Searches the tree for a value, considering the BST property"""

        this_node_value = self.value

        if this_node_value is not None:
            if this_node_value == query:
                return True 

            elif this_node_value > query:
                if self.left is not None:
                    return self.left._search_node_binary_search_tree(query)

            elif this_node_value < query:
                if self.right is not None:
                    return self.right._search_node_binary_search_tree(query)
        
        return False
    
    def _is_leaf(self) -> bool:
        """If node has no children, it is a leaf"""

        return bool(not self.right and not self.left)
    
    def _is_full(self) -> bool:
        """If node has two children, it is full"""
        return bool(self.right and self.left)


class BinaryTreeInterface():

    def __init__(self):
        self.root = Node()

    ############################
    #       Interface Methods
    ############################
    def add_node(self, value):
        """Adds a new node to the tree"""
        pass

    def search_node(self, value):
        """Searches the tree for a value"""
        pass

    ############################
    #       Public Methods
    ############################
    def is_leaf(self) -> bool:
        """Returns True if the node is a leaf"""

        if self.root is not None:
            return self.root._is_leaf()

    def is_full(self) -> bool:
        """Returns True if the node is full"""

        if self.root is not None:
            return self.root._is_full()

    def print_preorder(self):
        """Prints the BST in preorder"""
        
        if self.root is not None:
            self.root._repr_preorder()
    
    ############################
    #       Class Methods
    ############################
    @classmethod
    def is_balanced(cls, node, left=0, right=0) -> bool:
        """Returns True if the tree is balanced"""

        if node is None:
            return (left - right) < 2
        
        else:
            return cls.is_balanced(node.left, left + 1, right) and \
                            cls.is_balanced(node.right, left, right + 1)
    
    @classmethod
    def is_binary_search_tree(cls, node, min_node=None, max_node=None) -> bool:   
        """Returns True if the tree is a BST"""

        min_node = min_node or float('-inf')
        max_node = max_node or float('inf')

        if not node:
            return True
        
        if node.value < min_node or node.value > max_node:
            return False
        
        return cls.is_binary_search_tree(node.left, min_node, node.value) and \
                            cls.is_binary_search_tree(node.right, node.value, max_node)         

        

class BinaryTree(BinaryTreeInterface):
    """Implementation of a binary tree"""

    def add_node(self, value):
        """Adds a new node to the tree"""

        if self.root is None:
            self.root = Node(value)
        else:
            self.root._add_node_binary_tree(value)

    def search_node(self, value):
        """Searches the tree for a value"""

        if self.root:
            return self.root._search_node_preorder(value)


class BinarySearchTree(BinaryTreeInterface):
    
    def add_node(self, value):
        """Adds a new node to the tree"""

        if self.root is None:
            self.root = Node(value)
        else:
            self.root._add_node_binary_search_tree(value)

    def search_node(self, value):
        """Searches the tree for a value"""

        if self.root.value is not None:
            return self.root._search_node_binary_search_tree(value)

    @classmethod
    def largest_node(cls, node):
        """Returns the largest node in the tree"""

        if node.right:
            return cls.largest_node(node.right)
        else:
            return node
    
    @classmethod
    def smallest_node(cls, node):   
        """Returns the smallest node in the tree"""

        if node.left:
            return cls.smallest_node(node.left)
        else:
            return node
    



if __name__ == '__main__':

    ############################
    #   Test SimpleTree
    ############################
    print("\n\n🌴🌴🌴 Testing SimpleTree 🌴🌴🌴")
    t = SimpleTree('a', [SimpleTree('b', [SimpleTree('d'), SimpleTree('e')]), \
                            SimpleTree('c', [SimpleTree('h'), SimpleTree('g')])])
    print(t)


    ############################
    #   Test binary tree
    ############################
    print("\n\n🌳🌳🌳 Testing BinaryTree 🌳🌳🌳")
    bt = BinaryTree()
    array1 = [4, 1, 4, 6, 7, 9, 10, 5, 11, 5]
    print(f'\n🟡 Adding {array1} to the tree...')
    for i in array1:
        bt.add_node(i)
    print("🟢 Printing the tree in preorder...")   
    bt.print_preorder()
    print(f'\n🟢 Searching for node 5: {bt.search_node(5)}')
    print(f'❌ Searching for node 15: {bt.search_node(15)}')
    print(f'❌ Is root a leaf? {bt.is_leaf()}')
    print(f'🟢 Is root full? {bt.is_full()}')
    print(f'❌ Is the tree balanced? {BinaryTree.is_balanced(bt.root)}')
    print(f'❌ Is the tree a binary search tree? {BinaryTree.is_binary_search_tree(bt.root)}')



    ##############################
    #   Test binary search tree
    ##############################
    print("\n\n🎄🎄🎄 Testing BinarySearchTree 🎄🎄🎄")
    bst = BinarySearchTree()
    array1 = [4, 1, 4, 6, 7, 9, 10, 5, 11, 5]
    print(f'\n🟡 Adding {array1} to the tree...')
    for i in array1:
        bst.add_node(i)
    print("🟢 Printing the tree in preorder:")
    bst.print_preorder()
    print(f'\n🟢 Searching for node 5: {bst.search_node(5)}')
    print(f'❌ Searching for node 15: {bst.search_node(15)}')
    print(f'❌ Is root a leaf? {bst.is_leaf()}')
    print(f'🟢 Is root full? {bst.is_full()}')
    print(f'🟢 Largest node? {bst.largest_node(bst.root)}')
    print(f'🟢 Smallest node? {bst.smallest_node(bst.root)}')
    print(f'❌ Is the tree balanced? {bst.is_balanced(bst.root)}')
    print(f'🟢 Is the tree a binary search tree? {bst.is_binary_search_tree(bst.root)}')
