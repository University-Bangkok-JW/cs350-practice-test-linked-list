import cls

# Import the Node and SLinkedList classes from cls.py
Node = cls.Node
SLinkedList = cls.SLinkedList

# Pre data to be added to the linked list
array = [1, 2, 3, 4, 5]

# Create an SLinkedList object
list = SLinkedList()

list.predata(array)

print("Original Linked List:")
list.printLinkedList()

n = 2

list.delNode(n)

print("Linked List after delete", n)
list.printLinkedList()