class Node:
    def __init__(self, data):
        self.top = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        if self.top is None:
            return self.top is None
    
    def push(self, data):
        new_node = Node(data)
        if not self.top:
            self.top = new_node

        new_node.next = self.top
        self.top = new_node
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.top.data