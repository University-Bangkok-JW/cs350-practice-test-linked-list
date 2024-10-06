import cls

# Import the Node and SLinkedList classes from cls.py
Node = cls.Node
SLinkedList = cls.SLinkedList

# Create an SLinkedList object
list = SLinkedList()

# Our array to be added to the linked list
array = [1, 2, 3, 4, 5]

list.predata(array)

# Data to append to the linked list
data = 6

list.append(data)

# print the linked list
list.printLinkedList()