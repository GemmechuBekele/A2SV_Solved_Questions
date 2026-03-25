class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, head):
        new_queue = Node(head)
        if self.rear is None:
            self.rear = new_queue

        self.rear.next = new_queue
        self.rear = new_queue

    def dequeue(self):
        if self.front is None:
            return None
        
        deq = self.front.data
        self.front = self.front.next

        if self.front is None:  # queue becomes empty
            self.rear = None
            
        return deq