class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def convertedArray(self, head):
        array = []
        current = head
        while current:
            array.append(current.value)
            current = current.next
        return array
    
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3
res = node1.convertedArray(node1)
print(res)