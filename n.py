# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None

# list1 = Linkedlist()
# list1.head = Node("Jan")
# e2 = Node("feb")
# e3 = Node("mar")

# list1.head.next = e2
# e2.next = e3
# print(e3.data)



#Traversing

# class Node:
#     def __init__(self, data = None):
#         self.data = data
#         self.next = None
# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def listprint(self):
#         printval = self.head
#         while printval is not None:
#             print (printval.data)
#             printval = printval.next

# list = Linkedlist()
# list.head = Node(123)
# e2 = Node(456)
# e3 = Node(789)

# list.head.next = e2
# e2.next = e3

# list.listprint()



class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None


    def listprint(self):
        printval = self.head
        while printval in not None:
            print (printval.data)
            printval = printval.next


list = Linkedlist()
list.head = Node(12345)
e2 = Node(8368732678)
e3 = Node(376732732)

list.head.next = e2
e2.next = e3

list.listprint()












