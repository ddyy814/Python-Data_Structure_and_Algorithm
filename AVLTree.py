

# AVL
class Node(object):

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.rightChild = None
        self.leftChild = None


class AVL(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):

        if not node:
            return Node(data)

        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        node.height = max(self.calHeight(node.leftChild), self.calHeight(node.rightChild)) + 1

        return self.settleViolation(data, node)

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):

        if not node:
            return node

        # common operation code
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:

            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node...")
                del node
                return None

            if not node.leftChild:
                print("Removing a node with a right child...")
                tempNode = node.rightChild
                del node
                return tempNode

            elif not node.rightChild:
                print("Removing a node with a left child...")
                tempNode = node.leftChild
                del node
                return tempNode

            print("Removing node with two children...")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        if not node:
            return node  # if the tree had just a single node

        node.height = max(self.calHeight(node.leftChild), self.calHeight(node.rightChild)) + 1

        balance = self.calBalance(node)

        # doubly left heavy situation
        if balance > 1 and self.calBalance(node.leftChild) >= 0:
            return self.rotateRight(node)

        # left right case
        if balance > 1 and self.calBalance(node.leftChile) < 0:
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        # right right case
        if balance < -1 and self.calBalance(node.rightChild) <= 0:
            return self.rotateLeft(node)

        # right left case
        if balance < -1 and self.calBalance(node.rightChild) > 0:
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

    def getPredecessor(self, node):

        if node.rightChild:
            return self.getPredecessor(node.rightChild)

        return node

    def settleViolation(self, data, node):

        balance = self.calBalance(node)

        # case 1 --> left left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print("Left left heavy situation...")
            return self.rotateRight(node)

        # case 2 --> right right heavy situation --> single left rotation
        if balance < -1 and data > node.rightChild.data:
            print("Right right heavy situation...")
            return self.rotateLeft(node)

        # case 3 --> left right heavy situation
        if balance > 1 and data > node.leftChild.data:
            print("Left right heavy situation...")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        # case 4 --> Right left heavy situation
        if balance < -1 and data < node.rightChild.data:
            print("Left left heavy situation...")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

    def calHeight(self, node):

        if not node:
            return -1

        return node.height

    # if it return value > 1, it means it is a left heavy tree --> right rotation
    # .................. < -1, it means right heavy tree --> left rotation
    def calBalance(self, node):

        if not node:
            return 0

        return self.calHeight(node.leftChild) - self.calHeight(node.rightChild)

    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)

    def traverseInorder(self, node):

        if node.leftChild:
            self.traverseInorder(node.leftChild)

        print("%s" % node.data)

        if node.rightChild:
            self.traverseInorder(node.rightChild)

    def rotateRight(self, node):

        print("Rotating to the right on node ", node.data)

        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calHeight(node.leftChild), self.calHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calHeight(tempLeftChild.leftChild), self.calHeight(tempLeftChild.rightChild)) + 1

        return tempLeftChild

    def rotateLeft(self, node):

        print("Rotating to the left on node ", node.data)

        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t

        node.height = max(self.calHeight(node.leftChild), self.calHeight(node.rightChild)) + 1
        tempRightChild.height = max(self.calHeight(tempRightChild.leftChild), self.calHeight(tempRightChild.rightChild)) + 1

        return tempRightChild


avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(4)


avl.remove(5)
avl.remove(4)

avl.traverse()