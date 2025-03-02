

# Linked list insertion implementation

class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

# O(1)
    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def remove(self, data):
        if self.head is None:
            return

        self.size = self.size - 1
        currentNode = self.head
        previouseNode = None

        while currentNode.data != data:
            previouseNode = currentNode
            currentNode = currentNode.nextNode

        if previouseNode is None:
            self.head = currentNode.nextNode
        else:
            previouseNode.nextNode = currentNode.nextNode

# O(1)
    def size1(self):
        return self.size

# O(n)

    def insertEnd(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print('%d' % actualNode.data)
            actualNode = actualNode.nextNode


# Linked list test

linkedlist = LinkedList();


linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)

linkedlist.traverseList()
print(linkedlist.size1())

linkedlist.remove(12)
linkedlist.remove(122)
linkedlist.remove(3)
linkedlist.remove(31)


linkedlist.traverseList()
print(linkedlist.size1())

