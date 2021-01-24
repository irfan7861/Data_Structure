# class Pole:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None

# e1 = Linkedlist()
# e1.head = Pole('test')
# e2 = Pole(['abc', 123])  
# e3 = Pole(890)

# e1.head.next = e2
# e2.next = e3
# e4 =e3

# print(type(e2.data))



# class Node:
#     def __init__(self, data = None):
#         self.data = data
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def printlist (self):
#         printval = self.head
#         while printval is not None:
#             print(printval.head)
#             printval = printval.next 

# e1 = Linkedlist
# e1.head = Node(["abc", 345])
# e2 = Node()  
# e1.head.next = e2
# e3 = Node(("adad", 123, 766))  
# e2.next = e3  
# e4 = Node({"key" : 456})  
# e3.next = e4 
# e5 = Node({123,132,121,"dfg"})   
# e4.next = e5

# print(e1.head.data, e2.data, e3.data, e4.data, e5.data)

#stack Linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

# Check if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
# add data start of the stack
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def display(self):
        iternode = self.head
        if self.isempty():
            print("stack Underflow")

        else:

            while (iternode != None):

                print(iternode.data, "->", end = " ")
                iternode = iternode.next
            return                

Mystack = Stack()   

Mystack.push(11)
Mystack.push(22)
Mystack.push(33)
Mystack.push(44)

Mystack.display()










