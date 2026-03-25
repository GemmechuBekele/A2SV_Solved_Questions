class Queue:
    def __init__(self) -> None:
        self.q = []
    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.pop(0)
    def enqueue(self, value):
        self.q.append(value)