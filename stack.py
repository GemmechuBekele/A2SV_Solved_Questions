class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    # make sure to have constructor
    # constructor
    def __init__(self):
        self.top = None

    # isempty() -> boolean
        def isEmpty(self):
            return self.top is None
    # push
        def push(self, data):
            if not self.top:
                new_node = Node(data)
                self.top = new_node
            
            new_node.next = self.top
            self.top = new_node
    # pop
        def pop(self):
            if self.isEmpty():
                return None
            
            popped = self.top.data
            self.top = self.top.next
            return popped
    # peak
        def peek(self):
            if self.isEmpty():
                return None
            return self.top.data